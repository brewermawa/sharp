from django.contrib import admin
from django.forms import TextInput
from django.db import models

from .models import Announcement, BusinessInfo, Category, Brand, Product, Menu, Contact, Slider, Promo
from .models import ProductImages, ProductPrice, Feauture, FeautureValue, ProductFeautureValue, CategoryFilter
from .models import FooterSection, FooterLink


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
   list_display = ["announcement"]

   formfield_overrides = {
      models.CharField: {'widget': TextInput(attrs={'size':'60'})},
   }


@admin.register(BusinessInfo)
class BusinessInfoAdmin(admin.ModelAdmin):
   list_display = ["name", "street", "ext_number", "phone"]

   def has_add_permission(self, request):
        count = BusinessInfo.objects.all().count()

        if count == 0:
            return True
        
        return False
   
   
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ["name", "created_by", "created_date", "modified_by", "modified_date", "parent_category", "active"]
   list_filter = ["active", "created_by", "created_date", "modified_by", "modified_date"]
   list_editable = ("active",)
   prepopulated_fields = {"slug": ("name",)}
   readonly_fields = ["image_preview", "thumbnail_preview"]

   """
   save_model es el método que se ejecuta cuando se va a guardar el modelo. Como queremos que el campo created_by y modified_by
   tengan el usuario que está conectado al administrador, hacemos override del método. revisamos si change es falso, si
   es falso significa que se está insertando una nueva categoría y ponemos el campo created_by como el usuario conectado al 
   administrador. El campo modified by siempre se va a igualar al usuario conectado sin importar si se está insertando o 
   modificando la categoría
   """
   def save_model(self, request, obj, form, change):
      if not change:
         obj.created_by = request.user

      obj.modified_by = request.user
      return super().save_model(request, obj, form, change)
   
   def formfield_for_foreignkey(self, db_field, request, **kwargs):
      """
      El formfield_for_foreignkey lo usamos para filtrar las opciones que tenemos para seleccionar en el 
      drop down de parent_category

      El parent_category no puede ser la misma categoria ni ninguna otra que sea descendiente de ella, para esto hay que
      buscar estas categorías recursivamente

      Primero obtenemos el id de la categoría que estamos viendo: id = int(request.resolver_match.kwargs["object_id"]),
      inicializamos la lista de categorías excluídas y agregamos la categoría actual

      Definimos una función que obtiene todas las categorías que tienen como padre la categoria actual. Recorremos el 
      queryset obtenido (de categorías), la agregamos a la lista de categorías excluidas y corremos la misma función
      recursivamente hasta que terminemos de recorrer el árbol de categorias. Con esto obtenemos las categorías que no
      pueden ser padre de la categoria actual
      
      """
      if db_field.name == "parent_category":
         try:
            def get_categories(current_category_id):
               categories = Category.objects.filter(parent_category=current_category_id)

               for category in categories:
                  excluded_categories_id.append(category.pk)
                  get_categories(category.pk)

            id = int(request.resolver_match.kwargs["object_id"])
            excluded_categories_id = [id]
            get_categories(id)
            kwargs["queryset"] = Category.objects.all().exclude(pk__in=excluded_categories_id)
         except KeyError:
            pass
         
      return super().formfield_for_foreignkey(db_field, request, **kwargs)
   
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
   list_display = ["name"]
   prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ["name", "sku", "created_by", "created_date", "modified_by", "modified_date", "main_category", "active"]
   list_filter = ["active", "created_by", "created_date", "modified_by", "modified_date"]
   list_editable = ("active",)
   prepopulated_fields = {"slug": ("name",)}
   search_fields = ("name",)
   readonly_fields = ["thumbnail_preview"]


   def save_model(self, request, obj, form, change):
      if not change:
         obj.created_by = request.user

      obj.modified_by = request.user
      return super().save_model(request, obj, form, change)
    

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
   list_display = ["category", "product", "name", "order"]
   list_editable = ("order",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
   list_display = ["name", "email", "phone"]


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
   list_display = ["title", "name", "message", "active"]
   list_editable = ("active",)
   readonly_fields = ["image_preview"]


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
   list_display = ["title", "name", "message", "active"]
   list_editable = ("active",)
   readonly_fields = ["image_preview"]


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
   list_display = ["product", "name", "main"]
   readonly_fields = ["image_preview"]

   def save_model(self, request, obj, form, change):
      if obj.main:
         ProductImages.objects.filter(product=obj.product, main=True).update(main=False)

      super().save_model(request, obj, form, change)


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
   list_display = ["product", "name", "discount", "final_price", "active"]
   readonly_fields = ["final_price"]

   def save_model(self, request, obj, form, change):  
      if obj.discount_type == "p":
         obj.final_price = obj.product.price - (obj.product.price * (obj.discount / 100))
      else:
         obj.final_price = obj.product.price - obj.discount

      if obj.active:
         ProductPrice.objects.filter(product=obj.product, active=True).update(active=False)

      super().save_model(request, obj, form, change)


admin.site.register(Feauture)

@admin.register(FeautureValue)
class FeautureValueAdmin(admin.ModelAdmin):
   fields = ["feauture", "value"]

admin.site.register(ProductFeautureValue)

admin.site.register(CategoryFilter)

admin.site.register(FooterSection)

admin.site.register(FooterLink)