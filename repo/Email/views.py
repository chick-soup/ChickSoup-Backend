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

        data = serializer.initial_data
        if EmailService.check_email_exists(data["email"]) and EmailService.check_email_auth_status(data["email"]):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        EmailService.send_email(data["email"])
        return Response(data, status=status.HTTP_200_OK)
