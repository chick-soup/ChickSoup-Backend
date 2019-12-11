from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from User.services import (
    JWTService
)


class RefreshAPI(APIView):
    def get(self, request):
        pk = JWTService.run_auth_process(request.headers, 'refresh')

        return Response({'access_token': JWTService.create_access_token_with_id(pk)}, status=status.HTTP_200_OK)
