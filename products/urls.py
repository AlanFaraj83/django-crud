
from django.urls import path

from products.views import products, product_update, product_delete, product_delete_confirm

urlpatterns = [
    path('produtos/', products, name="products"),
    path('alterar-produto/<int:product_id>/', product_update, name="product_update"),
    path('remover-produto/<int:product_id>/', product_delete, name="product_delete"),
    path('confirmar-remocao-produto/<int:product_id>/', product_delete_confirm, name="product_delete_confirm"),

]
