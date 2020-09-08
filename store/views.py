from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item, Order, OrderItem

class HomeView(ListView):
    model = Item
    template_name = 'store/home-page.html'
    context_object_name = 'items'

class ItemView(DetailView):
    model = Item
    template_name = 'store/product-page.html'

def checkout(request):
    context = {
        'title': 'Checkout'
    }
    return render(request, 'store/checkout-page.html', context)

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.object.create(item=item)
    order = Order.objects.filter(user=request.user, orderd=False)