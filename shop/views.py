from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class HomeView(ListView):
    model = Product
    template_name = 'home.html'

class ShopView(ListView):
    model = Product
    template_name = 'shop/shop.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/single-product.html'
