from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from users.views import (account, login, login_settings, logout, UserRegistrationView,
                         wishlist)

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('account/', account, name='account'),
    path('login-settings/', login_settings, name='login-settings'),
    path('logout/', logout, name='logout'),
    path('wishlist/', wishlist, name='wishlist')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
