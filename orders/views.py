from http import HTTPStatus

from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from products.models import ShoppingCart
from orders.forms import OrderForm
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import stripe
from common.views import CommonContextMixin
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


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
            metadata={'order_id': self.object.id},
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:success')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:cancelled'))
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)


    def form_valid(self, form):
        form.instance.ordered_by = self.request.user
        return super(CheckoutCreateView, self).form_valid(form)


@csrf_exempt
def stripe_webhook_view(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
    # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
    session = stripe.checkout.Session.retrieve(
      event['data']['object']['id'],
      expand=['line_items'],
    )

    line_items = session.line_items
    # Fulfill the purchase...
    fulfill_order(line_items)

  # Passed signature verification
  return HttpResponse(status=200)

def fulfill_order(line_items):
  # TODO: fill me in
  print("Fulfilling order")


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
