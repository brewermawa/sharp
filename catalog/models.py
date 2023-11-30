from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.core.validators import RegexValidator


class Announcement(models.Model):
    announcement = models.CharField(max_length=60, help_text="Announcement text")

    def __str__(self):
        return self.announcement
    

class BusinessInfo(models.Model):
    name = models.CharField(max_length=60, help_text="Business Name (Razón Social)", verbose_name="Razón social")
    street = models.CharField(max_length=60 ,help_text="Street", verbose_name="Calle")
    ext_number = models.CharField(max_length=10 ,help_text="External number", verbose_name="Número exterior")
    int_number = models.CharField(max_length=10, help_text="Internal number", verbose_name="Número interior")
    neighbourhood = models.CharField(max_length=60, help_text="Colonia", verbose_name="Colonia")
    city = models.CharField(max_length=60, help_text="Munucipio", verbose_name="Municipio")
    state = models.CharField(max_length=60, help_text="Estado", verbose_name="Estado")
    zip_code = models.CharField(
        max_length=5,
        validators=[RegexValidator('^[0-9]{5}$')],
    )
    phone = models.CharField(
        max_length=13,
        validators=[RegexValidator('[(]?[0-9]{2,3}[)]?[-\s]?[0-9]{3,4}[-\s]?[0-9]{4}$')]
    )
    email = models.EmailField(max_length=100)

    class Meta:
        verbose_name = "Business Info"
        verbose_name_plural = "Business Info"


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True, help_text="Category name", verbose_name="name")
    slug = models.SlugField(max_length=60, unique=True, null=False, help_text="Friendly URl slug")
    short_description = models.TextField(verbose_name="Short description")
    large_description = models.TextField(verbose_name="Large description")
    image = models.ImageField(upload_to="category", help_text="Category image", verbose_name="Image", null=True, blank=True)
    thumbnail = models.ImageField(upload_to="category/thumbnail", help_text="Category thumbnail image", verbose_name="Thumbnail image", null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False, related_name="created_categories")
    created_date = models.DateField(auto_now_add=True, help_text="Creation date", null=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False, related_name="modified_categories")
    modified_date = models.DateField(auto_now_add=True, help_text="Modified date", null=True)
    active = models.BooleanField(default=True)
    parent_category = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True, unique=False, related_name="child_categories", help_text="The parent category", verbose_name="Parent category")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("catalog:category", kwargs={'slug': self.slug})
    
    def image_preview(self):
        return mark_safe(f"<img src='{self.image.url}' width='200' />")
    
    def thumbnail_preview(self):
        return mark_safe(f"<img src='{self.thumbnail.url}' width='100' />")
    

class Brand(models.Model):
    name = models.CharField(max_length=60, unique=True, help_text="Brand name", verbose_name="name")
    slug = models.SlugField(max_length=60, unique=True, null=False, help_text="Friendly URl slug")
    logo = models.ImageField(upload_to="brand", help_text="Brand logo", verbose_name="Brand logo")
    
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("catalog:brand", kwargs={'slug': self.slug})
    

class Product(models.Model):
    name = models.CharField(max_length=60, unique=True, help_text="Product name", verbose_name="name")
    slug = models.SlugField(max_length=60, unique=True, help_text="Friendly URL slug")
    sku = models.CharField(max_length=15, unique=True, help_text="Stock keeping unit", verbose_name="SKU")
    upc = models.CharField(max_length=12, unique=True, help_text="Universal product code", verbose_name="UPC")
    short_description = models.TextField(verbose_name="Short description")
    large_Description = models.TextField(verbose_name="Large description")
    thumbnail = models.ImageField(upload_to="product/thumbnail", help_text="Product thumbnail", verbose_name="Thumbnail image file", null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False, related_name="created_product")
    created_date = models.DateField(auto_now_add=True, help_text="Creation date", null=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False, related_name="modified_product")
    modified_date = models.DateField(auto_now_add=True, help_text="Modified date", null=True)
    active = models.BooleanField(default=True)
    main_category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, blank=False, related_name="products", help_text="The parent category of the product", verbose_name="Parent category")
    categories = models.ManyToManyField(Category, help_text="Other categories where the product should be shown")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="products", null=False, blank=False, help_text="The brand or manufacturer of the product")
    related_product = models.ManyToManyField("self", symmetrical=False, blank=True, related_name="related", help_text="Related products", verbose_name="Related products")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={'category_slug': self.main_category.slug, 'product_slug': self.slug})
    

class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    url = models.CharField(max_length=30, null=True, blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        if self.name:
            return self.name
        elif self.category:
            return self.category.name
        return self.product.name
    
    def get_absolute_url(self):
        return reverse(f"catalog:{self.url}")
    
    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"


class Contact(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False, verbose_name="name")
    email = models.EmailField(null=False, blank=False, max_length=100)
    phone = models.CharField(
        max_length=13,
        validators=[RegexValidator('[(]?[0-9]{2,3}[)]?[-\s]?[0-9]{3,4}[-\s]?[0-9]{4}$')]
    )
    message = models.TextField(default="")

    def __str__(self):
        return f"Mensaje de: {self.name}"
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"


class Slider(models.Model):
    title = models.CharField(max_length=60, unique=True, help_text="Slider title", verbose_name="Title")
    name = models.CharField(max_length=60, unique=True, help_text="Slider name", verbose_name="Name")
    message = models.CharField(max_length=60, unique=True, help_text="Slider message", verbose_name="Message")
    image = models.ImageField(upload_to="slider", help_text="Slider image", verbose_name="Image file", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="slider", null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="slider", null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

    def __str__(self):
        return self.title
    
    def image_preview(self):
        return mark_safe(f"<img src='{self.image.url}' width='200' />")
    

class Promo(models.Model):
    title = models.CharField(max_length=60, unique=True, help_text="Promo title", verbose_name="Title")
    name = models.CharField(max_length=60, unique=True, help_text="Promo name", verbose_name="Name")
    message = models.CharField(max_length=60, unique=True, help_text="Promo message", verbose_name="Message")
    image = models.ImageField(upload_to="promo", help_text="Promo image", verbose_name="Image file", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="promo", null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="promo", null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Promo"
        verbose_name_plural = "Promos"

    def __str__(self):
        return self.title
    
    def image_preview(self):
        return mark_safe(f"<img src='{self.image.url}' width='200' />")


class ProductImages(models.Model):
    name = models.CharField(max_length=60, unique=True, help_text="Image name", verbose_name="Name")
    image = models.ImageField(upload_to="product/", help_text="Product image", verbose_name="Product image file", null=True, blank=True)
    main = models.BooleanField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", null=True, blank=True)

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

    def __str__(self):
        return f"image '{self.name} for {self.product}'"
    
    def image_preview(self):
        return mark_safe(f"<img src='{self.image.url}' width='200' />")
    

class ProductPrice(models.Model):
    PERCENTAGE = "p"
    DIRECT = "d"
    PRICING_TYPE_CHOICES = [
        (PERCENTAGE, "Percentage"),
        (DIRECT, "Direct"),
    ]

    name = models.CharField(max_length=60, unique=True, help_text="Pricing name", verbose_name="Name")
    discount_type = models.CharField(max_length=1, choices=PRICING_TYPE_CHOICES, default=PERCENTAGE)
    discount = models.DecimalField(max_digits=7, decimal_places=2)
    active = models.BooleanField(default=False)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    final_price = models.DecimalField(max_digits=7, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pricing", null=True, blank=True)

    def __str__(self):
        return self.name

    

    
