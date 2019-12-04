import jwt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Friend.serializers import RegisterFriendSerializers
from Friend.models import FriendsList
from conf.settings import SECRET_KEY


class RegisterFriendAPI(APIView):
    def post(self, request):
        token = jwt.decode(request.headers['token'], key = SECRET_KEY, algorithms='HS256')
        serializer = RegisterFriendSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.initial_data

        guest_id = data['guest_id']

        FriendsList(
            host_id = token,
            guest_id = guest_id
        ).save()


        return Response({
            "status":"OK"
        }, 200)