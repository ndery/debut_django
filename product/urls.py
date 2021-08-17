from django.urls import path
from .views import add_product, edit_product, index, product_list, detail_product, remove_product

urlpatterns = [
    path("", index, name="index"),
    path("products/", product_list, name="product_list"),
    path("products/<int:product_id>", detail_product, name="detail_product"),
    path("products/add/", add_product, name="add_product"),
    path("products/<int:product_id>/edit/", edit_product, name="edit_product"),
    path("products/<int:product_id>/remove/", remove_product, name="remove_product")
    ]