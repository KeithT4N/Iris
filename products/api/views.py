from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import (
    Stall,
    Product
)

from products.serializers import (
    StallSerializer,
    StallUpdateSerializer,
    ProductSerializer
)

class StallList(APIView):
    def get(self, request):
        queryset = Stall.objects.all()
        serializer = StallSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self):
        pass


class StallDetail(APIView):
    def get_object(self, stall_id):
        try:
            return Stall.objects.get(pk = stall_id)
        except:
            raise Http404

    def get(self, request, stall_id):
        stall = self.get_object(stall_id)
        serializer = StallSerializer(stall)
        return Response(serializer.data)

    

    def delete(self, request, stall_id):
        stall = self.get_object(stall_id)



class StallUpdate(APIView):
    def get(self, request):
        queryset = Stall.objects.all()
        serializer = StallUpdateSerializer(queryset, many = True)
        return Response(serializer.data)



class ProductList(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self):
        pass

