from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from User.services import (
    JWTService,
    UserService
)
from User.exceptions import UserNotFound
from .services import KakaoIdService


class MyKakaoIdAPI(APIView):
    def get(self, request):
        pk = JWTService.run_auth_process(request.headers)

        if not UserService.check_pk_exists(pk):
            raise UserNotFound

        return Response({"kakao_id": KakaoIdService.check_kakao_id_with_pk(pk)}, status=status.HTTP_200_OK)
