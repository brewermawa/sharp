from django.shortcuts import render


def home(request):
    return render(request, "catalog/home.html")

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