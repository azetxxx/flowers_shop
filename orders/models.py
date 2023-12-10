from django.db import models

from users.models import User


class Order(models.Model):
    PENDING = 0
    PROCESSING = 1
    CANCELLED = 2
    OUT_FOR_DELIVERY = 3
    DELIVERED = 4
    REFUNDED = 5
    STATUSES = (
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (CANCELLED, 'Cancelled'),
        (OUT_FOR_DELIVERY, 'Out for delivery'),
        (DELIVERED, 'Delivered'),
        (REFUNDED, 'Refunded'),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    address1 = models.CharField(max_length=256)
    address2 = models.CharField(max_length=256, blank=True, null=True)
    country = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=64)
    orders_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=PROCESSING, choices=STATUSES)
    ordered_by = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order #{self.id} from {self.first_name} {self.last_name}'
