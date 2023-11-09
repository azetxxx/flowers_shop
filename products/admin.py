from django.contrib import admin

from products.models import Color, Holiday, Season, Flower, Product


admin.site.register(Color)
admin.site.register(Holiday)
admin.site.register(Season)
admin.site.register(Flower)
admin.site.register(Product)
