from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Item, Order, OrderItem
from django.utils import timezone
from django.contrib import messages

class HomeView(ListView):
    model = Item
    template_name = 'home-page.html'
    context_object_name = 'items'
    paginate_by = 10

class ItemView(DetailView):
    model = Item
    template_name = 'product-page.html'

def checkout(request):
    context = {
        'title': 'Checkout'
    }
    return render(request, 'checkout-page.html', context)

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # Check if the item in order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'This item quantity add onther ')
            return redirect("product", slug=slug)
        else:
            messages.info(request, 'This item was added to your cart')
            order.items.add(order_item)
            return redirect("product", slug=slug)

    else:
        order = Order.objects.create(user=request.user, orderd_date=timezone.now())
        order.items.add(order_item)
        messages.info(request, 'A new order was create')
        return redirect("product", slug=slug)




def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # Check if the item in order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, 'This item was remove to your cart')
            return redirect("product", slug=slug)

        else:
            messages.info(request, 'This item was not in your cart')
            return redirect("product", slug=slug)

    else:
        messages.info(request, 'You dont have order ')
        return redirect("product", slug=slug)
