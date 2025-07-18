from django.urls import path
from .views import ProductListCreateView, CustomerListCreateView, OrderListCreateView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
]
