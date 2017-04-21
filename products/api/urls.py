from django.conf.urls import url
from django.contrib import admin

from .views import (
    StallAPIView,
    ProductAPIView
)

app_name = 'products'
urlpatterns = [
    url(r'^$', StallAPIView.as_view(), name = 'list')
]