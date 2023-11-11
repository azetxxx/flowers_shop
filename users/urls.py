from django.urls import path

from users.views import registration, login, account, login_settings, logout, wishlist
from django.conf.urls.static import static

from django.conf import settings

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('account/', account, name='account'),
    path('login-settings/', login_settings, name='login-settings'),
    path('logout/', logout, name='logout'),
    path('wishlist/', wishlist, name='wishlist')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)