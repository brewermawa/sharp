from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("category/", views.category, name="category"),
    path("product/", views.product, name="product"),
    path("promotions/", views.promotions, name="promotions"),
    path("compare/", views.compare, name="compare"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("guide/", views.guide, name="guide"),
]