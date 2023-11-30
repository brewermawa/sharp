from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.home, name="home"),
    path("<slug:slug>", views.category, name="category"),
    path("<slug:category_slug>/<slug:product_slug>/", views.product, name="product"),
    path("category/", views.category, name="category"),
    path("product/", views.product, name="product"),
    path("promotions/", views.promotions, name="promotions"),
    path("compare/", views.compare, name="compare"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("guide/", views.guide, name="guide"),
    path("contacto/", views.contact, name="contacto"),
]