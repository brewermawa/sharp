from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("<slug:category_slug>", views.category_view, name="category"),
    path("<slug:category_slug>/<slug:product_slug>/", views.product_view, name="product"),
    path("category/", views.category_view, name="category"),
    path("product/", views.product_view, name="product"),
    path("promotions/", views.promotions_view, name="promotions"),
    path("compare/", views.compare_view, name="compare"),
    path("wishlist/", views.wishlist_view, name="wishlist"),
    path("guide/", views.guide_view, name="guide"),
    path("contacto/", views.contact_view, name="contacto"),
]