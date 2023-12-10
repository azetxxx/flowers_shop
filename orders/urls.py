from django.contrib.auth.decorators import login_required
from django.urls import path

from orders.views import (CancelledTemplateView, CheckoutCreateView,
                          SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('checkout/', login_required(CheckoutCreateView.as_view()), name='checkout'),
    path('success/', SuccessTemplateView.as_view(), name='success'),
    path('cancelled/', CancelledTemplateView.as_view(), name='cancelled'),

]
