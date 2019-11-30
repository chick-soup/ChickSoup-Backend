from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    EmailCheckSerializers
)


class EmailCheckAPI(APIView):
    def post(self, request):
        serializer = EmailCheckSerializers(data=request.data)
        if serializer.is_valid():
            return Response(serializer.initial_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
