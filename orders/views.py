from http import HTTPStatus

import stripe
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from common.views import CommonContextMixin
from orders.forms import OrderForm
from products.models import ShoppingCart

stripe.api_key = settings.STRIPE_SECRET_KEY


class CheckoutCreateView(CommonContextMixin, CreateView):
    template_name = 'orders/checkout.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:checkout')
    title = 'Checkout 🌼 Fun Flowers'

    def post(self, request, *args, **kwargs):
        super(CheckoutCreateView, self).post(request, *args, **kwargs)
        cart_items = ShoppingCart.objects.filter(user=self.request.user)
        checkout_session = stripe.checkout.Session.create(
            line_items=cart_items.stripe_products(),
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


def fulfill_order(session):
    order_id = int(session.metadata.order_id)



class SuccessTemplateView(CommonContextMixin, TemplateView):
    template_name = 'orders/success.html'
    title = 'Success 🌼 Fun Flowers'


class CancelledTemplateView(CommonContextMixin, TemplateView):
    template_name = 'orders/cancelled.html'
    title = 'Cancelled 🌼 Fun Flowers'
