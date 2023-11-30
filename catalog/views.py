from django.shortcuts import render
from django.core.mail import EmailMessage, get_connection
from django.conf import settings    

from .forms import ContactForm
from .models import Slider, Promo, Product, ProductImages, ProductPrice


def home(request):
    sliders = Slider.objects.filter(active=True)
    promos = Promo.objects.filter(active=True)
    products = Product.objects.filter(categories__name="home")
    productList = []

    for product in products:
        try:
            productImage = f"images/{ProductImages.objects.get(product=product, main=True).image}"
        except:
            productImage = ""

        try:
            price = ProductPrice.objects.get(product=product, active=True).final_price
            notPrice = product.price
            discount = ((notPrice - price) / notPrice)*100
        except:
            price = product.price
            notPrice = False
            discount = False

        product = {
            "name": product.name,
            "brand": product.brand,
            "image": productImage,
            "price": price,
            "notPrice": notPrice,
            "discount": discount
        }
        productList.append(product)

    return render(request, "catalog/home.html", {
        "sliders": sliders,
        "promos": promos,
        "products": productList,
    })

def category(request):
    return render(request, "catalog/category.html")

def product(request):
    return render(request, "catalog/product.html")

def promotions(request):
    return render(request, "catalog/promotions.html")

def compare(request):
    return render(request, "catalog/compare.html")

def wishlist(request):
    return render(request, "catalog/wishlist.html")

def guide(request):
    return render(request, "catalog/selection_guide.html")

def contact(request):
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