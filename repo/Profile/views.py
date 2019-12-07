from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from User.services import JWTService


class MyProfileAPI(APIView):
    def get(self, request):
        pk = JWTService.run_auth_process(request.headers)

        return Response({"id": pk}, status=status.HTTP_200_OK)
