from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import OrderItem, Order


def add_to_cart(request, slug):
    user = request.user
    item = get_object_or_404(OrderItem, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        user=user,
        item=item,
        ordered=False
    )
    order_qs = Order.objects.filter(user=user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__item=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'This item quantity was updated.')
            return redirect('chat:home')
        else:
            order.items.add(order_item)
            messages.info(request, 'This item was added to your cart.')
            return redirect('chat:home')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=user,
            ordered_date= ordered_date
        )
        order.items.add(order_item)
        messages.info(request, 'This item was added to your cart.')
        return redirect('chat:home')
        
