from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    EmailCheckSerializers
)
from .services import (
    EmailService
)


class EmailCheckAPI(APIView):
    def post(self, request):
        serializer = EmailCheckSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.initial_data["email"]
        if EmailService.check_email_exists(email) and EmailService.check_email_auth_status(email):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        EmailService.delete_email_if_exist(email)
        EmailService.send_email(email, code="asdfa323s")
        return Response({"email": email}, status=status.HTTP_200_OK)
