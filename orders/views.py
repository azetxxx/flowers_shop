from http import HTTPStatus

from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from products.models import ShoppingCart
from orders.forms import OrderForm
from django.http import HttpResponseRedirect

import stripe
from common.views import CommonContextMixin
from django.conf import settings


stripe.api_key = 'sk_test_51IUWRPFTrBbkHWRlurWewrD18UU0sSFoKCjHBlOyoOUqF7xGZPehrRLFa1oeJRWQ7wnac6pcn7L4orqog75szEHr008wdBEkYr'


class CheckoutCreateView(CommonContextMixin, CreateView):
    template_name = 'orders/checkout.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:checkout')
    title = 'Checkout 🌼 Fun Flowers'

    def post(self, request, *args, **kwargs):
        super(CheckoutCreateView, self).post(request, *args, **kwargs)

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1OL3ziFTrBbkHWRlGbbsSELB',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:success')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:cancelled'))
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)


    def form_valid(self, form):
        form.instance.ordered_by = self.request.user
        return super(CheckoutCreateView, self).form_valid(form)


    # success_url = reverse_lazy('orders:order_create')
    # title = 'Order 🛒 Fun Store'

    # def post(self, request, *args, **kwargs):
    #     super(OrderCreateView, self).post(request, *args, **kwargs)
    #     baskets = Basket.objects.filter(user=self.request.user)
    #     checkout_session = stripe.checkout.Session.create(
    #         line_items=baskets.stripe_products(),
    #         metadata={'order_id': self.object.id},
    #         mode='payment',
    #         success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_success')),
    #         cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_canceled')),
    #     )
    #     return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)




# def checkout(request):
#     shopping_cart = ShoppingCart.objects.all()

#     context = {
#         'title': 'Checkout 🌼 Fun Flowers',
#         'shopping_cart': shopping_cart,
#     }
#     return render(request, 'orders/checkout.html', context)


class SuccessTemplateView(CommonContextMixin, TemplateView):
    template_name = 'orders/success.html'
    title = 'Success 🌼 Fun Flowers'

    # def get(self, request, *args, **kwargs):
    #     code = kwargs['code']
    #     user = User.objects.get(email=kwargs['email'])
    #     email_verifications = EmailVerification.objects.filter(user=user, code=code)
    #     if email_verifications.exists() and not email_verifications.first().is_expired():
    #         user.is_verified_email = True
    #         user.save()
    #         return super(EmailVerificationView, self).get(request, *args, **kwargs)
    #     else:
    #         return HttpResponseRedirect(reverse('index'))


class CancelledTemplateView(CommonContextMixin, TemplateView):
    template_name = 'orders/cancelled.html'
    title = 'Cancelled 🌼 Fun Flowers'
