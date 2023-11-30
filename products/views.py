from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from common.views import CommonContextMixin

from products.models import User, Product, ProductCategory, ShoppingCart


class IndexView(CommonContextMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Home 🌼 Fun Flowers'


class ProductsListView(CommonContextMixin, ListView):
    model = Product
    template_name = 'products/shop.html'
    title = 'Shop 🌼 Fun Flowers'
    paginate_by = 6

    def get_queryset(self, **kwargs):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset.all()

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['current_category_id'] = self.kwargs.get('category_id')
        return context


class ProductDetailsView(CommonContextMixin, TemplateView):
    template_name = 'products/details.html'
    title = 'Details: 🌼 Fun Flowers'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailsView, self).get_context_data(**kwargs)
        product_id = self.kwargs.get('product_id')
        context['item'] = Product.objects.get(id=product_id)
        return context


class CartListView(CommonContextMixin, TemplateView):
    template_name = 'products/cart.html'
    title = 'Cart 🌼 Fun Flowers'


    # def get_context_data(self, **kwargs):
    #     context = super(CartListView, self).get_context_data()
    #     context["shopping_cart"] = ShoppingCart.objects.filter(user=self.request.user)
    #     return context

    # def get_queryset(self):
    #     return ShoppingCart.objects.filter(user=self.request.user)




# @login_required
# def cart(request):
#     cart_subtotal = None
#     cart_total = None
#     context = {
#         'title': 'Cart 🌼 Fun Flowers',
#         'shopping_cart': ShoppingCart.objects.filter(user=request.user)
#     }

#     return render(request, 'products/cart.html', context)


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
