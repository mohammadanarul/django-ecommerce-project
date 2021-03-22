from django.urls import path
from .views import (
    add_to_cart,
    single_item_remove_form_cart,
    OrderDetails,
)

app_name = 'orders'
urlpatterns = [
    path('cart-details/', OrderDetails.as_view(), name='cart_details'),
    path('add-to-cart/<slug>/', add_to_cart, name='add_item_to_cart'),
    path('single-item-remove-from-cart/<slug>/', single_item_remove_form_cart, name='single_item_remove_from_cart'),
]
