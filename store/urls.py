from django.urls import path
from .views import (
    HomeView, 
    ItemView,
    checkout
)

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('checkout/', checkout, name="checkout"),
    path('product/<slug>/', ItemView.as_view(), name="product"),
]