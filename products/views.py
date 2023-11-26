from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.views.generic.base import TemplateView

from products.models import ProductCategory, Product, ShoppingCart
from django.core.paginator import Paginator


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context["title"] = "Home 🌼 Fun Flowers"
        return context


def shop(request, category_id=None, page_number=1):

    product_items = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    items_per_page = 6
    paginator = Paginator(product_items, items_per_page)
    products_on_page = paginator.page(page_number)

    context = {
        'title': 'Shop: 🌼 Fun Flowers',
        'categories': ProductCategory.objects.all(),
        'products': products_on_page,
    }
    return render(request, 'products/shop.html', context)


def details(request):
    context = {
        'title': 'Shop: 🌼 Fun Flowers',
    }
    return render(request, 'products/details.html', context)



@login_required
def cart(request):

    cart_subtotal = None
    cart_total = None

    context = {
        'title': 'Cart 🌼 Fun Flowers',
        'shopping_cart': ShoppingCart.objects.filter(user=request.user)
    }

    return render(request, 'products/cart.html', context)


@login_required
def add_item_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item = ShoppingCart.objects.filter(user=request.user, product=product)

    if not cart_item.exists():
        ShoppingCart.objects.create(user=request.user, product=product, quantity=1)
    else:
        cart_item = cart_item.first()
        cart_item.quantity += 1
        cart_item.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def remove_item_from_cart(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        cart_item = ShoppingCart.objects.get(product=product, user=request.user)
        cart_item.delete()
    except ShoppingCart.DoesNotExist:
        print('❌ Item not found in the cart.')

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def checkout(request):
    shopping_cart = ShoppingCart.objects.all()

    context = {
        'title': 'Checkout 🌼 Fun Flowers',
        'shopping_cart': shopping_cart,
    }
    return render(request, 'products/checkout.html', context)
