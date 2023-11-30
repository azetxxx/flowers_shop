from products.models import ShoppingCart


def shopping_cart(request):
    user = request.user
    return {'cart_items': ShoppingCart.objects.filter(user=user) if user.is_authenticated else []}
