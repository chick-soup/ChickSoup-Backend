from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from User.services import (
    JWTService,
    UserService
)
from User.exceptions import UserNotFound
from Friend.services import FriendService
from .services import KakaoIdService
from .exceptions import (
    InvalidKakaoId
)


class MyKakaoIdAPI(APIView):
    def get(self, request):
        pk = JWTService.run_auth_process(request.headers)

        return Response({"kakao_id": KakaoIdService.get_kakao_id_with_pk(pk)}, status=status.HTTP_200_OK)


class KakaIdAPI(APIView):
    def get(self, request, kakao_id):
        host_id = JWTService.run_auth_process(request.headers)

        if not KakaoIdService.check_kakao_id_exist(kakao_id):
            raise InvalidKakaoId

        profile = KakaoIdService.get_profile_with_kakao_id(kakao_id)
        guest_id = profile.user_id.id

        return Response({
            "id": guest_id,
            "nickname": profile.nickname,
            "myself": True if host_id == guest_id else False,
            "relate": FriendService.check_relationship(id1=host_id, id2=guest_id)
        }, status=status.HTTP_200_OK)
