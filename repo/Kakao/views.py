from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from User.services import (
    JWTService,
    UserService
)
from User.exceptions import UserNotFound
from .services import KakaoIdService
from .exceptions import (
    InvalidKakaoId
)


class MyKakaoIdAPI(APIView):
    def get(self, request):
        pk = JWTService.run_auth_process(request.headers)

        if not UserService.check_pk_exists(pk):
            raise UserNotFound

        return Response({"kakao_id": KakaoIdService.get_kakao_id_with_pk(pk)}, status=status.HTTP_200_OK)


class KakaoProfileAPI(APIView):
    def get(self, request, kakao_id):
        pk = JWTService.run_auth_process(request.headers)

        if not UserService.check_pk_exists(pk):
            raise UserNotFound

        if not KakaoIdService.check_kakao_id_exits(kakao_id):
            raise InvalidKakaoId

        profile = KakaoIdService.get_profile_with_kakao_id(kakao_id)

        return Response({
            "id": profile.user_id.id,
            "nickname": profile.nickname,
            "myself": True if pk == profile.user_id.id else False
        }, status=status.HTTP_200_OK)
