from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    EmailCheckSerializers,
    EmailAuthSerializers
)
from .services import (
    EmailService,
    Random,
)
from .exceptions import (
    EmailExists,
    EmailNotRequestAuth,
    AuthCodeDoseNotMatch
)


# 이메일과 인증 코드를 받아서 인증을 완료시키는 API
class EmailAuthAPI(APIView):
    def post(self, request):
        serializer = EmailAuthSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        email = data["email"]
        if not EmailService.check_email_exists(email):
            raise EmailNotRequestAuth

        if EmailService.check_email_exists(email) and EmailService.check_email_auth_status(email):
            raise EmailExists

        if data["auth_code"] != EmailService.check_email_auth_code(email):
            raise AuthCodeDoseNotMatch

        EmailService.email_auth_complete(email)
        return Response(data, status=status.HTTP_200_OK)


# 이메일 중복 확인 및 인증 코드 발송 API
class EmailCheckAPI(APIView):
    def post(self, request):
        serializer = EmailCheckSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.initial_data["email"]
        if EmailService.check_email_exists(email) and EmailService.check_email_auth_status(email):
            raise EmailExists

        EmailService.delete_email_if_exist(email)

        auth_code = Random.create_random_string(10)
        EmailService.send_email(email, code=auth_code)

        EmailService.create_email_queryset(email=email, auth_code=auth_code)
        return Response({"email": email}, status=status.HTTP_200_OK)
