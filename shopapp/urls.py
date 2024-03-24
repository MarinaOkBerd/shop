from django.urls import path
from . import views
from .views import customer_orders, customer_products, product_by_id, order_products, add_product_form

urlpatterns = [
    path('', views.shopapp, name='shopapp'),
    path('customers/', views.customers, name='customers'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('customers/<int:customer_id>', customer_orders, name='customer_orders'),
    path('customers/<int:customer_id>/products/', customer_products, name='customer_products'),
    path('products/<int:product_id>', product_by_id, name='product_id'),
    path('orders/<int:order_id>', order_products, name='order_products'),
    path('products/add', add_product_form, name='add_product_form'),
]