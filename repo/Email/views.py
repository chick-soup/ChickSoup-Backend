from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    EmailCheckSerializers
)
from .services import (
    EmailService,
    Random,
)
from .exceptions import (
    EmailExists
)


class EmailCheckAPI(APIView):
    def post(self, request):
        serializer = EmailCheckSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.initial_data["email"]
        if EmailService.check_email_exists(email) and EmailService.check_email_auth_status(email):
            raise EmailExists

        EmailService.delete_email_if_exist(email)

        auth_code = Random.create_random_string()
        EmailService.send_email(email, code=auth_code)

        EmailService.create_email_queryset(email=email, auth_code=auth_code)
        return Response({"email": email}, status=status.HTTP_200_OK)
