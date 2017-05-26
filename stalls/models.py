from django.db.models import (
    Model,
    CharField,
    IntegerField,
    DateTimeField,
)

from django.db.models.signals import pre_delete
from django.dispatch import receiver


# Create your models here.
class Stall(Model):
    name = CharField(max_length = 64)

    date_updated = DateTimeField(auto_now = True)
    date_created = DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class StallTombstone(Model):
    stall_id = IntegerField(unique = True, primary_key = True)
    deletion_date = DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.stall_id)


@receiver(pre_delete, sender = Stall)
def delete_stall(sender, instance, **kwargs):
    StallTombstone.objects.create(stall_id = instance.id)