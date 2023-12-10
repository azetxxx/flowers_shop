import stripe
from django.conf import settings
from django.db import models

from users.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    is_available = models.BooleanField()
    image = models.ImageField(upload_to='products_images')
    stripe_product_price_id = models.CharField(max_length=128, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.stripe_product_price_id:
            stripe_product_price = self.create_stripe_product_price()
            self.stripe_product_price_id = stripe_product_price['id']
        super(Product, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def create_stripe_product_price(self):
        stripe_product = stripe.Product.create(name=self.name)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'],
            unit_amount=int(self.price * 100),
            currency='eur',
        )
        return stripe_product_price


class ShoppingCartQuerySet(models.QuerySet):
    def cart_subtotal(self):
        return sum(item.product_total() for item in self)

    def total_quantity(self):
        return sum(item.quantity for item in self)

    def stripe_products(self):
        line_items = []
        for item in self:
            item = {
                'price': item.product.stripe_product_price_id,
                'quantity': item.quantity,
            }
            line_items.append(item)
        return line_items


class ShoppingCart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = ShoppingCartQuerySet.as_manager()

    def __str__(self):
        return f'\
            Cart for {self.user.username} | \
            Product (ID {self.product.id}): {self.product.name} | \
            Qty: {self.quantity}'

    def product_total(self):
        return self.product.price * self.quantity


# class Discount(models.Model):
#     code = models.CharField(max_length=64)
#     start_date = models.DateTimeField(blank=True, null=True)
#     end_date = models.DateTimeField(blank=True, null=True)
#     multiple_usage = models.BooleanField()
#     percent = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
#     amount = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2)
#     user_email = models.EmailField(blank=True, null=True)

#     def __str__(self):
#         return f'Discount code: {self.code} | \
#               Value: {self.percent} % or {self.amount} $ | \
#               For Email: {self.user_email}'
