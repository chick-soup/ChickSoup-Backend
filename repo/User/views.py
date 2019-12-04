import jwt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Email.services import EmailService
from Email.exceptions import EmailExists
from .exceptions import (
    UnauthenticatedEmail,
    UserNotFound
)
from .serializers import (
    SignUpSerializers,
    ProfileSerializers
)
from .services import (
    UserService,
    HashService,
    JWTService
)


class SignUpProfileAPI(APIView):
    def post(self, request):
        pk = JWTService.run_auth_process(request.headers)

        serializer = ProfileSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.initial_data
        if not UserService.check_pk_exists(pk):
            raise UserNotFound

        UserService.update_user_profile(pk, data["nickname"], data["status_message"])
        return Response(pk, status=status.HTTP_200_OK)


class SignUpAPI(APIView):
    def post(self, request):
        serializer = SignUpSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.initial_datal
        _email = data["email"]
        _password = data["password"]

        if not (EmailService.check_email_exists(_email) and EmailService.check_email_auth_status(_email)):
            raise UnauthenticatedEmail

        if UserService.check_email_exists(_email):
            raise EmailExists

        pk = UserService.create_new_user(_email, HashService.hash_string_to_password(_password))

        return Response({'access_token': JWTService.create_access_token_with_id(pk)}, status=status.HTTP_200_OK)