from django.contrib import admin
from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = (
        'id',
        'created',
        ('first_name', 'last_name'),
        'email',
        'address1',
        'address2',
        'country',
        'city',
        'zip_code',
        'orders_history',
        'status',
        'ordered_by'
        )
    readonly_fields  = ('id', 'created')
