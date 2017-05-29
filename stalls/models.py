from django.db.models import (
    Model,
    CharField,
    IntegerField,
    DateTimeField,
)


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