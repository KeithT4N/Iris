from stalls.models import Stall, StallTombstone
from stalls.serializers import StallSerializer

def get_updates_since(date):
    new_stalls = Stall.objects.filter(date_created__gt = date)
    modified_stalls = Stall.objects.filter(date_updated__gt = date).exclude(date_created__gt = date)
    deleted_stalls = StallTombstone.objects.filter(deletion_date__gt = date)

    new_stalls = StallSerializer(new_stalls, many = True).data
    modified_stalls = StallSerializer(modified_stalls, many = True).data
    deleted_stalls = [tombstone.stall_id for tombstone in deleted_stalls]

    return {
        "new": new_stalls,
        "modified": modified_stalls,
        "deleted": deleted_stalls
    }
