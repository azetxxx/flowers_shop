from django.urls import path

from company.views import about, contact, gallery
from django.conf.urls.static import static

from django.conf import settings

app_name = 'company'

urlpatterns = [
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)