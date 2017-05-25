from rest_framework.serializers import ModelSerializer, SlugRelatedField

from products.models import (
    Product,
    ProductTag
)

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
        fields = ['id', 'name', 'price', 'stall', 'description', 'quantity', 'stall']
        read_only_fields = ['tags',]

