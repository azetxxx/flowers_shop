from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from company.views import AboutView, ContactView, GalleryView

app_name = 'company'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
