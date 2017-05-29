from channels import Group
from urllib.parse import parse_qs
from rest_framework.authtoken.models import Token


secure_group = "Iris_WebSockets"


def ws_connect(message):
    params = parse_qs(message.content['query_string'])
    token = params.get('token', (None,))[0]

    if not token:
        message.reply_channel.send({"accept": False})
        return

    user = Token.objects.filter(key = token)

    if not user:
        message.reply_channel.send({"accept": False})
        return

    message.reply_channel.send({"accept": True})
    Group(secure_group).add(message.reply_channel)


def ws_receive(message):
    # Nothing to do here
    pass


def ws_disconnect(message):
    Group(secure_group).discard(message.reply_channel)

