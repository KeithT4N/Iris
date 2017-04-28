from datetime import datetime
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from stalls.models import Stall

from products.models import (
    Product,
    ProductTag
)
from products.serializers import (
    ProductSerializer,
    ProductUpdateSerializer
)

def save_tags(tags, product):
    product_tags_set = product.producttag_set.all()
    old_tags = []

    # Convert ProductTag object to string
    for product_tag in product_tags_set:
        old_tags.append(product_tag.content)

    differences = get_differences(old_tags, new_tags = tags)

    for tag in differences["removed"]:
        removed_tag = product_tags_set.get(content = tag)
        removed_tag.delete()

    for tag in differences["added"]:
        new_tag = ProductTag(content = tag, product = product)
        new_tag.save()


def get_differences(old_tags, new_tags):
    removed = []
    added = []

    for tag in old_tags:
        if tag not in new_tags:
            removed.append(tag)

    for tag in new_tags:
        if tag not in old_tags:
            added.append(tag)

    return {"added": added, "removed": removed}


class ProductList(APIView):
    def get(self, request):

        stall_id = request.GET.get('stall_id')

        if stall_id:
            try:
                stall = Stall.objects.get(pk = stall_id)
                queryset = Product.objects.all().filter(stall)
            except:

                # The stall is not found and the database throws an error.
                # In this case, set queryset to a blank.
                queryset = Product.objects.none()

        else:
            queryset = Product.objects.all()

        serializer = ProductSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self, request):

        if "stall_id" not in request.data:
            return Response(data = {
                "error": "stall_id not found in JSON data"
            }, status = status.HTTP_400_BAD_REQUEST)


        stall_id = request.data["stall_id"]

        try:
            stall = Stall.objects.get(pk = stall_id)
        except:
            return Response(data = {
                "error": "Stall not found"
            }, status = status.HTTP_400_BAD_REQUEST)

        serializer = ProductSerializer(data = request.data)


        if not serializer.is_valid():
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        product = serializer.save()

        if "tags" in request.data:
            save_tags(request.data["tags"], product)

        stall.last_updated = datetime.now() #Update stall when products are added to it
        stall.save()

        return Response(serializer.data, status = status.HTTP_201_CREATED)



class ProductDetail(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(pk = product_id)
        except:
            raise Http404

    def get(self, request, product_id):
        product = self.get_object(product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, product_id):
        product = self.get_object(product_id)
        serializer = ProductSerializer(product, data = request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        serializer.save()

        if "tags" in request.data:
            save_tags(request.data["tags"], product)

        return Response(serializer.data, status = status.HTTP_201_CREATED)

    def delete(self, request, product_id):
        product = self.get_object(product_id)
        stall = product.stall
        product.delete()

        stall.last_updated = datetime.now() #Update stall when products are deleted
        stall.save()

        return Response(status = status.HTTP_204_NO_CONTENT)

class ProductUpdate(APIView):
    def get(self):
        queryset = Product.objects.all()
        serializer = ProductUpdateSerializer(queryset, many = True)
        return Response(serializer.data)
