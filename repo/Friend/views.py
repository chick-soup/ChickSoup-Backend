from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Friend.serializers import RegisterFriendSerializers


class RegisterFriendAPI(APIView):
    def post(self, request):
        serializer = RegisterFriendSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.initial_data

        guest_id = data['guest_id']

        

        return Response("TEST", 200)