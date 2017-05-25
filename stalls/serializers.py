from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField
)

from stalls.models import Stall

class StallSerializer(ModelSerializer):
    products = SlugRelatedField(source = 'product_set', slug_field = 'pk', many = True, read_only = True)

    class Meta:
        model = Stall
        fields = ['id', 'name', 'products',]
