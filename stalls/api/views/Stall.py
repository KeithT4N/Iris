from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import Stall
from stalls.Serializers import (
    StallSerializer,
    StallUpdateSerializer
)

class StallList(APIView):

    def get(self, request):
        queryset = Stall.objects.all()
        serializer = StallSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StallSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


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

    def put(self, request, stall_id):
        stall = self.get_object(stall_id)
        serializer = StallSerializer(stall, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, stall_id):
        stall = self.get_object(stall_id)
        stall.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class StallUpdate(APIView):

    def get(self, request):
        queryset = Stall.objects.all()
        serializer = StallUpdateSerializer(queryset, many = True)
        return Response(serializer.data)
