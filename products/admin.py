from django.contrib import admin
from products.models import (
    Stall,
    Product
)

admin.site.register(Stall)
admin.site.register(Product)
