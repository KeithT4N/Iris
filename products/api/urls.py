from django.conf.urls import url
from django.contrib import admin

from .views import (
    StallList,
    StallUpdate,
    StallDetail,
    ProductList
)

app_name = 'products'
urlpatterns = [
    url(r'^$', StallList.as_view()),
    url(r'^update/$', StallUpdate.as_view()),
    url(r'^(?P<stall_id>(\d+))/$', StallDetail.as_view()),
    # url(r'^/(?P<stall_id>(\d+))/products',)
]