from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from shop.models import Product
from .models import OrderItem, Order
from django.contrib import messages
from django.views.generic import DetailView, View

class OrderDetails(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        template_name = 'shop/cart-summary.html'
        return render(self.request, template_name, {'object': order})

def add_to_cart(request, slug):
    user = request.user
    item = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        user=user,
        item=item,
        ordered=False
    )
    order_qs = Order.objects.filter(user=user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'This item quantity was updated.')
            return redirect('order:cart_details')
        else:
            order.items.add(order_item)
            messages.info(request, 'This item was added to your cart.')
            return redirect('order:cart_details')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=user,
            ordered_date= ordered_date
        )
        order.items.add(order_item)
        messages.info(request, 'This item was added to your cart.')
        return redirect('shop:home')

def single_item_remove_form_cart(request, slug):
    user = user.request
    item = get_object_or_404(Product, slug=slug)
    order_qs = OrderItem.objects.filter(
        user = user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                user=user,
                item=item,
                ordered=False
            )
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.item.remove(order_item)
            messages.info(request, 'This item quantity was updated.')
            return redirect('shop:home')
        else:
            messages.info(request, 'This item was not in your cart.')
            return redirect('shop:home')
    else:
        messages.info(request, 'You do not have an active order.')
        return redirect('shop:home')




        
