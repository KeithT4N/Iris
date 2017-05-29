from django.conf.urls import url
from rest_framework.authtoken import views as rest_framework_views

from .views import (
    sign_in,
    sign_up,
    sign_out,
    require_username_password,
)

urlpatterns = [
    url(r'^sign_in/$', require_username_password(sign_in)),
    url(r'^sign_up/$', require_username_password(sign_up)),
    url(r'^sign_out/$', sign_out),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name = 'get_auth_token'),
]
