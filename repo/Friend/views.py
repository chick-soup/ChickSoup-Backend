from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .services import (
    FriendService
)
from .exceptions import (
    FriendNotFound,
    AlreadyRequest,
    AlreadyFriend,
    Myself
)
from User.services import (
    JWTService,
    UserService
)
from Kakao.services import (
    KakaoIdService
)


class KakaoIdAddFriendAPI(object):
    @staticmethod
    def post(request, kakao_id):
        host_id = JWTService.run_auth_process(request.headers)

        if not KakaoIdService.check_kakao_id_exist(kakao_id):
            raise FriendNotFound

        guest_id = KakaoIdService.get_pk_with_kakao_id(kakao_id)

        if host_id == guest_id:
            raise Myself
        if FriendService.check_if_friend_or_not(host_id=host_id, guest_id=guest_id):
            if FriendService.check_if_friend_or_not(host_id=guest_id, guest_id=host_id):
                raise AlreadyFriend
            raise AlreadyRequest

        FriendService.create_new_friend(host_id=host_id, guest_id=guest_id)

        if FriendService.check_if_friend_or_not(host_id=guest_id, guest_id=host_id):
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_200_OK)

