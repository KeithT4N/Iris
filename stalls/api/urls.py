from django.conf.urls import url

from stalls.api.views.Stall import (
    StallList,
    StallUpdate,
    StallDetail,
)

urlpatterns = [
    url(r'^$', StallList.as_view()),
    url(r'^update/$', StallUpdate.as_view()),
    url(r'^(?P<stall_id>(\d+))/$', StallDetail.as_view()),
]
