from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import (
    Stall,
    Product
)
from products.serializers import (
    ProductSerializer
)

def get_stall(stall_id):
    try:
        return Stall.objects.get(pk = stall_id)
    except:
        raise Http404

class ProductList(APIView):
    def get(self, request, stall_id):
        stall = get_stall(stall_id)
        queryset = Product.objects.all().filter(stall = stall)
        serializer = ProductSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, stall_id):
        get_stall(stall_id) #Throw when does not exist
        request.data['stall'] = stall_id #TODO: Make something less hacky

        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(pk = product_id)
        except:
            raise Http404

    def get(self, request, product_id, stall_id):
        pass
