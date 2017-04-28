from rest_framework.serializers import ModelSerializer, SlugRelatedField
from stalls.models import Stall

class StallSerializer(ModelSerializer):
    products = SlugRelatedField(source = 'product_set', slug_field = 'pk', many = True, read_only = True)

    class Meta:
        model = Stall
        fields = '__all__'



class StallUpdateSerializer(ModelSerializer):
    # Stall product can be accessed via stall_instance.product_set.all()
    # Use ProductUpdateSerializer to process Stall Products

    class Meta:
        model = Stall
        fields = ('id', 'last_updated')
