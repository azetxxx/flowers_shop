from django.shortcuts import render

from products.models import Product, Color, Flower, Holiday, Season

# Create your views here.


def index(request):
    context = {
        'title': 'Start 🌼 Fun Flowers',
    }
    return render(request, 'products/index.html', context)


def shop(request):
    context = {
        'title': 'Shop: 🌼 Fun Flowers',
        'products': Product.objects.all(),
        'colors': Color.objects.all(),
        'flowers': Flower.objects.all(),
        'holidays': Holiday.objects.all(),
        'seasons': Season.objects.all(),
    }
    return render(request, 'products/shop.html', context)


def details(request):
    context = {
        'title': 'Shop: 🌼 Fun Flowers',
    }
    return render(request, 'products/details.html', context)


def cart(request):
    context = {
        'title': 'Cart 🌼 Fun Flowers',
    }
    return render(request, 'products/cart.html', context)


def checkout(request):
    context = {
        'title': 'Checkout 🌼 Fun Flowers',
    }
    return render(request, 'products/checkout.html', context)
