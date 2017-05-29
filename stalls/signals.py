from json import dumps
from channels import Group
from django.dispatch import receiver

from Iris.consumers import secure_group
from stalls.serializers import StallSerializer
from stalls.models import Stall, StallTombstone

from django.db.models.signals import post_delete, post_save


@receiver(post_delete, sender = Stall)
def delete_stall(sender, instance, **kwargs):
    StallTombstone.objects.create(stall_id = instance.id)
    group = Group(secure_group)

    message = {
        'type' : 'deletion',
        'model': 'Stall',
        'id'   : instance.id
    }

    group.send({
        "text": dumps(message)
    })


@receiver(post_save, sender = Stall)
def save_stall(sender, instance, created, **kwargs):
    instance_serialized = StallSerializer(instance, many = False).data

    message = {
        'type'    : 'creation' if created else 'modification',
        'model'   : 'Stall',
        'instance': instance_serialized
    }

    Group(secure_group).send({
        "text": dumps(message)
    })
