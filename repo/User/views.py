import jwt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Email.services import EmailService, ClientService
from Email.exceptions import EmailExists, NotPermissionEmail
from .exceptions import (
    UnauthenticatedEmail,
    UserNotFound,
    IdAndPwNotMatch,
    IdNotExist
)
from .serializers import (
    SignUpSerializers,
    ProfileSerializers,
    LoginSerializers
)
from .services import (
    UserService,
    HashService,
    JWTService,
    S3Service
)


class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.initial_data
        _email = data["email"]
        if not UserService.check_email_exists(_email):
            raise IdNotExist

        user = UserService.get_user_by_email(_email)
        if not HashService.compare_pw_and_hash(data["password"], user.password):
            raise IdAndPwNotMatch

        return Response({
            "access_token": JWTService.create_access_token_with_id(user.id, int(request.data['minute'])) if 'minute' in request.data else JWTService.create_access_token_with_id(user.id),
            "refresh_token": JWTService.create_refresh_token_with_id(user.id)
        }, status=status.HTTP_200_OK)


class SignUpProfileAPI(APIView):
    def post(self, request):
        pk = JWTService.run_auth_process(request.headers)

        serializer = ProfileSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.initial_data
        profile = request.FILES.get('profile')
        if profile is not None:
            S3Service.upload_profile(pk, profile, S3Service.make_s3_resource())

        UserService.update_user_profile(pk, data["nickname"])
        return Response({"id": pk}, status=status.HTTP_200_OK)


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
        if EmailService.check_email_auth_ip(_email) != ClientService.get_client_ip(request):
            raise NotPermissionEmail

        pk = UserService.create_new_user(_email, HashService.hash_string_to_password(_password))
        return Response({'access_token': JWTService.create_access_token_with_id(pk)}, status=status.HTTP_200_OK)
