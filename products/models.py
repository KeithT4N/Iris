from stalls.models import Stall

from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    IntegerField,
    DecimalField,
    DateTimeField,
    PositiveIntegerField,
    CASCADE
)

from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Product(Model):
    name = CharField(max_length = 64)
    price = DecimalField(decimal_places = 2, max_digits = 10)
    stall = ForeignKey(Stall, on_delete = CASCADE)
    description = CharField(max_length = 256)
    quantity = PositiveIntegerField()

    date_updated = DateTimeField(auto_now = True)
    date_created = DateTimeField(auto_now_add = True)


    def __str__(self):
        return "{0} - {1}".format(self.name, self.stall)


class ProductTag(Model):
    content = CharField(max_length = 32)
    product = ForeignKey(Product, on_delete = CASCADE)

    def __str__(self):
        return self.content


class ProductTombstone(Model):
    product_id = IntegerField(unique = True, primary_key = True)
    deletion_date = DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.product_id

@receiver(pre_delete, sender = Product)
def delete_product(sender, instance, **kwargs):
    ProductTombstone.objects.create(product_id = instance.id)
