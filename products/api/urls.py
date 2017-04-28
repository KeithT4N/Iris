from django.conf.urls import url


from .views.Product import (
    ProductList,
    ProductUpdate,
    ProductDetail,
)

urlpatterns = [
    url(r'^$', ProductList.as_view()),
    url(r'^update/$', ProductUpdate.as_view()),
    url(r'^(?P<product_id>(\d+))/$', ProductDetail.as_view()),
]
