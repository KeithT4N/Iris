from .forms import UserForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth import (
    login,
    logout,
    authenticate
)


def require_username_password(get_response):

    @api_view(['POST'])
    @permission_classes((AllowAny,))
    def middleware(request):

        if 'username' not in request.data or 'password' not in request.data:
            return Response({
                'error': 'Invalid Request'
            }, status = status.HTTP_400_BAD_REQUEST)

        response = get_response(request)

        return response

    return middleware


def sign_in(request):
    username = request.data['username']
    password = request.data['password']

    user = authenticate(username = username, password = password)

    if user is not None:
        login(request, user)
        return Response(status = status.HTTP_200_OK)

    return Response(data = {
        'error': 'Invalid Credentials'
    }, status = status.HTTP_401_UNAUTHORIZED)


def sign_up(request):
    form = UserForm(request.data)

    if not form.is_valid():
        return Response(data = {
            'error': 'Invalid Request'
        }, status = status.HTTP_400_BAD_REQUEST)

    user = form.save(commit = False)
    password = request.data['password']
    user.set_password(password)
    user.save()

    return Response(status = status.HTTP_200_OK)


@api_view(['GET'])
def sign_out(request):
    logout(request)
    return Response(status = status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def is_logged_in(request):
    if request.user.is_authenticated():
        return Response( data = {
            "is_logged_in": True,
            "username"    : request.user.username
        })
    else:
        return Response( data = { "is_logged_in": False })
