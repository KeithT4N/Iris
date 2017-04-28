from django.db.models import (
    Model,
    CharField,
    DateTimeField
)

# Create your models here.
class Stall(Model):
    name = CharField(max_length = 64)

    last_updated = DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

