from django.conf.urls import url

from .views.Stall import (
    StallList,
    StallUpdate,
    StallDetail,
)

from .views.Product import (
    ProductList
)

urlpatterns = [
    url(r'^$', StallList.as_view()),
    url(r'^update/$', StallUpdate.as_view()),
    url(r'^(?P<stall_id>(\d+))/$', StallDetail.as_view()),
    url(r'^(?P<stall_id>(\d+))/products/$', ProductList.as_view())
]
