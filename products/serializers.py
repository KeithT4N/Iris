from rest_framework.serializers import ModelSerializer, SlugRelatedField

from products.models import (
    Product,
    ProductTag
)

class TagSerializer(ModelSerializer):
    class Meta:
        model = ProductTag
        fields = ['content']


class ProductSerializer(ModelSerializer):

    '''
    Make output appear as an array of strings:
    "tags": ["first", "second", "third"]
    
    Rather than an array of objects:
    "tags": [{
        "content": "first"
    }, 
        "content": "second"
    }]
    '''
    tags = SlugRelatedField(source = 'producttag_set',
                            slug_field = 'content',
                            many = True,
                            read_only = True)

    class Meta:
        model = Product
        fields = '__all__'


# Update Serializers

class ProductUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'last_updated')

