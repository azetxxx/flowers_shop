from django.urls import path


from orders.views import SuccessView, CheckoutView

app_name = 'orders'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('success/', SuccessView.as_view(), name='success'),

]
