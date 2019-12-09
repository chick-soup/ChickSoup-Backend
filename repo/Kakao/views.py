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
from Friend.views import KakaoIdAddFriendAPI


class MyKakaoIdAPI(APIView):
    def get(self, request):
        pk = JWTService.run_auth_process(request.headers)

        return Response({"kakao_id": KakaoIdService.get_kakao_id_with_pk(pk)}, status=status.HTTP_200_OK)


class KakaIdAPI(APIView):
    def get(self, request, kakao_id):
        pk = JWTService.run_auth_process(request.headers)

        if not KakaoIdService.check_kakao_id_exist(kakao_id):
            raise InvalidKakaoId

        profile = KakaoIdService.get_profile_with_kakao_id(kakao_id)

        return Response({
            "id": profile.user_id.id,
            "nickname": profile.nickname,
            "myself": True if pk == profile.user_id.id else False
        }, status=status.HTTP_200_OK)

    def post(self, request, kakao_id):
        return KakaoIdAddFriendAPI.post(request, kakao_id)
