from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.dateparse import parse_datetime

from stalls import update_compiler
from stalls.models import Stall
from stalls.serializers import StallSerializer


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
    @staticmethod
    def get_object(stall_id):
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

        date_string = request.query_params.get('last_updated', None)

        if date_string is None:
            return Response(data = {
                "error": "Date not provided in request"
            }, status = status.HTTP_400_BAD_REQUEST)

        date = parse_datetime(date_string)

        if date is None:
            return Response(data = {
                "error": "Unable to parse datetime"
            }, status = status.HTTP_400_BAD_REQUEST)

        updates = update_compiler.get_updates_since(date)

        return Response(updates)
