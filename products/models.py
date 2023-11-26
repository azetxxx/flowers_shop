
from django.db import models

from users.models import User

# Create your models here.


# class Color(models.Model):
#     name = models.CharField(max_length=128)

#     def __str__(self):
#         return self.name


# class Holiday(models.Model):
#     name = models.CharField(max_length=128)

#     def __str__(self):
#         return self.name


# class Season(models.Model):
#     name = models.CharField(max_length=128)

#     def __str__(self):
#         return self.name


# class Flower(models.Model):
#     name = models.CharField(max_length=128)
#     color = models.ForeignKey(to=Color, on_delete=models.CASCADE, null=True, blank=True)
#     season = models.ForeignKey(to=Season, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return self.name


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
    # color = models.ForeignKey(to=Color, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # holiday = models.ForeignKey(to=Holiday, on_delete=models.CASCADE, null=True, blank=True)
    # main_flower = models.ForeignKey(to=Flower, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class ShoppingCartQuerySet(models.QuerySet):
    def cart_subtotal(self):
        return sum(item.product_total() for item in self)


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
