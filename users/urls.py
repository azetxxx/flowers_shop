from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (OrderListView, UserLoginSettingsView, UserLoginView,
                         UserProfileView, UserRegistrationView, wishlist)

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/order-history/', login_required(OrderListView.as_view()), name='order-history'),
    path('profile/<int:pk>/login-settings/', login_required(UserLoginSettingsView.as_view()), name='login-settings'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('wishlist/', wishlist, name='wishlist')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
