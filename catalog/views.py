from django.shortcuts import render
from django.core.mail import EmailMessage, get_connection
from django.conf import settings    

from .forms import ContactForm
from .models import Slider, Promo, Product, ProductImages, ProductPrice, Category
from .utils import getBreadCrumbs, getProducts


def home_view(request):
    sliders = Slider.objects.filter(active=True)
    promos = Promo.objects.filter(active=True)
    products = getProducts(Product.objects.filter(categories__pk=1))

    return render(request, "catalog/home.html", {
        "sliders": sliders,
        "promos": promos,
        "products": products,
    })

def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = getProducts(Product.objects.filter(categories__pk=category.pk))

    breadCrumbs = getBreadCrumbs(category.pk, [])
    breadCrumbs.reverse()

    childCategories = Category.objects.filter(parent_category=category.id)

    return render(request, "catalog/category.html", {
        "breadCrumbs": breadCrumbs,
        "category": category,
        "childCategories": childCategories,
        "products": products,
    })

def product_view(request, category, product):
    return render(request, "catalog/product.html")

def promotions_view(request):
    return render(request, "catalog/promotions.html")

def compare_view(request):
    return render(request, "catalog/compare.html")

def wishlist_view(request):
    return render(request, "catalog/wishlist.html")

def guide_view(request):
    return render(request, "catalog/selection_guide.html")

def contact_view(request):
    confirm = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            confirm = True  

            with get_connection(host=settings.EMAIL_HOST, port=settings.EMAIL_PORT, username=settings.EMAIL_HOST_USER, 
                                password=settings.EMAIL_HOST_PASSWORD, use_tls=settings.EMAIL_USE_TLS) as connection:  
                subject = f"Comentario web de {form.cleaned_data['name']}"
                message = f"email: {form.cleaned_data['email']}"
                message += f"Teléfono: {form.cleaned_data['phone']}"
                message += f"Comentario: {form.cleaned_data['message']}"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ["mguerra@bi-tecnologia.com"]  
                EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
    else:
        form =  ContactForm ()

    return render(request, "catalog/contact.html", {
        "contact_form": form,
        "confirm": confirm,
    })