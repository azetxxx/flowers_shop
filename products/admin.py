from django.contrib import admin

from products.models import Product, ProductCategory, ShoppingCart

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description')
    fields = ('image', 'name', 'description', ('price', 'is_available'), 'stripe_product_price_id', 'category')
    readonly_fields = ('description',)
    search_fields = ('name', 'description')
    ordering = ('-name',)


class ShoppingCartAdmin(admin.ModelAdmin):
    model = ShoppingCart
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
