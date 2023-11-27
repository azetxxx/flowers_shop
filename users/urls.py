from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.decorators import login_required

from users.views import (UserProfileView, UserLoginSettingsView, login, logout, UserRegistrationView,
                         wishlist, OrderListView)

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/order-history/', login_required(OrderListView.as_view()), name='order-history'),
    path('profile/<int:pk>/login-settings/', login_required(UserLoginSettingsView.as_view()), name='login-settings'),
    path('logout/', logout, name='logout'),
    path('wishlist/', wishlist, name='wishlist')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
