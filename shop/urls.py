from django.urls import path
from .views import (
    HomeView,
    ShopView,
    )

app_name = 'shop'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
]