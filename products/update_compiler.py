from products.models import Product, ProductTombstone
from products.serializers import ProductSerializer

def get_updates_since(date):
    new_products = Product.objects.filter(date_created__gt = date)
    modified_products = Product.objects.filter(date_updated__gt = date).exclude(date_created__gt = date)
    deleted_products = ProductTombstone.objects.filter(deletion_date__gt = date)

    new_products = ProductSerializer(new_products, many = True).data
    modified_products = ProductSerializer(modified_products, many = True).data
    deleted_products = [tombstone.product_id for tombstone in deleted_products]

    return {
        "new": new_products,
        "modified": modified_products,
        "deleted": deleted_products
    }