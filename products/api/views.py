from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import (
    Stall,
    Product
)

from products.serializers import (
    StallSerializer,
    ProductSerializer
)


class StallAPIView(APIView):
    def get(self, request):
        stalls = Stall.objects.all()
        serializer = StallSerializer(stalls, many = True)
        return Response(serializer.data)

    def post(self):
        pass


class StallUpdateAPIVIew(APIView):
    def get(self, request):



class ProductAPIView(APIView):
    def get(self):
        pass

    def post(self):
        pass

