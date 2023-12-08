from django.urls import path
from django.contrib.auth.decorators import login_required

from orders.views import SuccessTemplateView, CancelledTemplateView, CheckoutCreateView

app_name = 'orders'

urlpatterns = [
    path('checkout/', CheckoutCreateView.as_view(), name='checkout'),
    path('success/', SuccessTemplateView.as_view(), name='success'),
    path('cancelled/', CancelledTemplateView.as_view(), name='cancelled'),

]
