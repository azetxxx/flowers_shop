from django.urls import path

from products.views import shop, details, cart, checkout
from django.conf.urls.static import static

from django.conf import settings

app_name = 'products'

urlpatterns = [
    path('', shop, name='index'),
    path('cart/', cart, name='cart'),
    path('details/', details, name='details'),
    path('cart/checkout/', checkout, name='checkout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)