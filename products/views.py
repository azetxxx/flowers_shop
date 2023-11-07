from django.shortcuts import render

from products.models import Product, Color, Flowers, Holiday, Season

# Create your views here.


def index(request):
    context = {
        'page_title': 'Start: 🌼 Fun Flowers',
    }
    return render(request, 'products/index.html', context)


def shop(request):
    context = {
        'page_title': 'Shop: 🌼 Fun Flowers',
        'products': Product.objects.all(),
        'colors': Color.objects.all(),
        'flowers': Flowers.objects.all(),
        'holidays': Holiday.objects.all(),
        'seasons': Season.objects.all(),
    }
    return render(request, 'products/shop.html', context)
