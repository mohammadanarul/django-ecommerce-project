from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

class HomeView(ListView):
    model = Product
    template_name = 'home.html'

class ShopView(ListView):
    model = Product
    template_name = 'shop/shop.html'
