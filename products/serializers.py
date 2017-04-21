from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    IntegerField,
    DecimalField
)

from products.models import (
    Stall,
    Product
)

class StallSerializer(ModelSerializer):
    class Meta:
        model = Stall
        fields = '__all__'

class StallUpdateSerializer(ModelSerializer):
    class Meta:
        model = Stall
        fields = ('pk', 'last_updated')

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'last_updated')