from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Email.services import EmailService
from Email.exceptions import EmailExists
from .exceptions import (
    UnauthenticatedEmail
)
from .serializers import (
    SignUpSerializers
)
from .services import (
    UserService,
    HashService
)


class SignUpAPI(APIView):
    def post(self, request):
        serializer = SignUpSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.initial_data
        _email = data["email"]
        _password = data["password"]

        if not (EmailService.check_email_exists(_email) and EmailService.check_email_auth_status(_email)):
            raise UnauthenticatedEmail

        if UserService.check_email_exists(_email):
            raise EmailExists

        UserService.create_new_user(_email, HashService.hash_string_to_password(_password))

        return Response(data, status=status.HTTP_200_OK)


class RegisterFriendApi(APIView):
    def post(self, request):
        #TODO
        pass


class FindFriendApi(APIView):
    def get(self, request):
        #TODO
        pass