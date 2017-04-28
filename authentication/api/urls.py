from django.conf.urls import url

from .views import (
    # sign_in,
    sign_up,
    sign_out,
    is_logged_in,
    require_username_password,
)

urlpatterns = [
    # url(r'^signin/$', require_username_password(sign_in)),
    url(r'^signup/$', require_username_password(sign_up)),
    url(r'^signout/$', sign_out),
    url(r'^logincheck/$', is_logged_in)
]
