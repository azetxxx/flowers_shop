from django.urls import path

from products.views import shop
from django.conf.urls.static import static

from django.conf import settings

app_name = 'products'

urlpatterns = [
    path('', shop, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)