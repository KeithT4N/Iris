from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import (
    Stall,
    Product,
    ProductTag
)
from products.serializers import (
    ProductSerializer
)


def get_stall(stall_id):
    try:
        return Stall.objects.get(pk = stall_id)
    except:
        raise Http404


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
    def get(self, request, stall_id):
        stall = get_stall(stall_id)
        queryset = Product.objects.all().filter(stall = stall)
        serializer = ProductSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, stall_id):
        get_stall(stall_id)  # Throw when does not exist
        request.data['stall'] = stall_id  # TODO: Make something less hacky

        serializer = ProductSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get_object(self, product_id, stall_id):
        stall = get_stall(stall_id)
        try:
            return Product.objects.get(pk = product_id, stall = stall)
        except:
            raise Http404

    def get(self, request, product_id, stall_id):
        product = self.get_object(product_id, stall_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, product_id, stall_id):
        product = self.get_object(product_id, stall_id)
        serializer = ProductSerializer(product, data = request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        serializer.save()

        if "tags" in request.data:
            save_tags(request.data["tags"], product)

        return Response(serializer.data, status = status.HTTP_201_CREATED)

    def delete(self, request, product_id, stall_id):
        product = self.get_object(product_id, stall_id)
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class ProductUpdate(APIView):
    pass
