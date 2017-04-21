from rest_framework.serializers import ModelSerializer

from products.models import (
    Stall,
    Product
)


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class StallSerializer(ModelSerializer):
    products = ProductSerializer(source = 'product_set', many = True, required = False)

    class Meta:
        model = Stall
        fields = '__all__'


# Update Serializers

class ProductUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'last_updated')


class StallUpdateSerializer(ModelSerializer):
    # Stall product can be accessed via stall_instance.product_set.all()
    # Use ProductUpdateSerializer to process Stall Products
    products = ProductUpdateSerializer(source = 'product_set', many = True)

    class Meta:
        model = Stall
        fields = ('id', 'last_updated', 'products')
