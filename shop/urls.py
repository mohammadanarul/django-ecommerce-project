from django.urls import path
from .views import (
    HomeView,
    ShopView,
    ProductDetailView,
    )

app_name = 'shop'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('product-detail/<slug>/', ProductDetailView.as_view(), name='product_detail'),
]