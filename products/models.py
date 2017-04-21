from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    DecimalField,
    DateTimeField,
    PositiveIntegerField,
    CASCADE
)


class Stall(Model):
    name = CharField(max_length = 64)

    last_updated = DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length = 64)
    price = DecimalField(decimal_places = 2, max_digits = 5)
    stall = ForeignKey(Stall, on_delete = CASCADE)
    description = CharField(max_length = 256)
    quantity = PositiveIntegerField()

    last_updated = DateTimeField(auto_now = True)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.stall)
