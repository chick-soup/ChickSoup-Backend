from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegisterFriendAPI(APIView):
    def post(self, request):

        return Response("TEST", 200)