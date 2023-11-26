from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from products.views import (ProductsListView, add_item_to_cart, cart, checkout,
                            details, remove_item_from_cart)

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('cart/', cart, name='cart'),
    path('details/', details, name='details'),
    path('cart/checkout/', checkout, name='checkout'),
    path('cart/add/<int:product_id>/', add_item_to_cart, name='add-item-to-cart'),
    path('cart/remove/<int:product_id>/', remove_item_from_cart, name='remove_item_from_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
