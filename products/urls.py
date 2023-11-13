from django.urls import path

from products.views import shop, details, cart, checkout, add_item_to_cart, remove_item_from_cart
from django.conf.urls.static import static

from django.conf import settings

app_name = 'products'

urlpatterns = [
    path('', shop, name='index'),
    path('category/<int:category_id>/', shop, name='category'),
    path('page/<int:page_number>/', shop, name='paginator'),
    path('cart/', cart, name='cart'),
    path('details/', details, name='details'),
    path('cart/checkout/', checkout, name='checkout'),
    path('cart/add/<int:product_id>/', add_item_to_cart, name='add-item-to-cart'),
    path('cart/remove/<int:product_id>/', remove_item_from_cart, name='remove_item_from_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)