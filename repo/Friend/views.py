from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .services import (
    FriendService,
    UserPutAPIService
)
from .exceptions import (
    PutBadRequest,
    FriendNotFound,
    AlreadyRequest,
    AlreadyFriend,
    Myself,
    NotFriend,
    SameStatus
)
from User.services import (
    JWTService,
    UserService
)
from Kakao.services import (
    KakaoIdService
)


class FriendListAPI(APIView):
    def get(self, request):
        pk = JWTService.run_auth_process(request.headers)

        friend_list = FriendService.sort_list(FriendService.get_friend_list(pk))
        return Response(FriendService.convert_list_to_dict(friend_list), status=status.HTTP_200_OK)


class MuteListAPI(APIView):
    def get(self, request):
        pk = JWTService.run_auth_process(request.headers)

        friend_list = FriendService.sort_list(FriendService.get_friend_list(pk))
        filter_friend_list = FriendService.filter_if_mute_false(friend_list)

        return Response(FriendService.convert_list_to_dict(filter_friend_list), status=status.HTTP_200_OK)


class HiddenListAPI(APIView):
    def get(self, request):
        pk = JWTService.run_auth_process(request.headers)

        friend_list = FriendService.sort_list(FriendService.get_friend_list(pk))
        filter_friend_list = FriendService.filter_if_hidden_false(friend_list)

        return Response(FriendService.convert_list_to_dict(filter_friend_list), status=status.HTTP_200_OK)


class FriendRequestListAPI(APIView):
    def get(self, request):
        pk = JWTService.run_auth_process(request.headers)

        return Response(status=status.HTTP_200_OK)


class UserIdFriendAPI(APIView):
    def delete(self, request, guest_id):
        host_id = JWTService.run_auth_process(request.headers)

        if not UserService.check_pk_exists(guest_id):
            raise FriendNotFound
        if host_id is guest_id:
            raise Myself
        if not FriendService.check_both_friend(host_id, guest_id):
            raise NotFriend

        FriendService.delete_friend(host_id, guest_id)
        return Response(status=status.HTTP_200_OK)

    def put(self, request, guest_id):
        host_id = JWTService.run_auth_process(request.headers)

        if UserPutAPIService.check_put_bad_request(request.data):
            raise PutBadRequest
        if not UserService.check_pk_exists(guest_id):
            raise FriendNotFound
        if host_id is guest_id:
            raise Myself
        if not FriendService.check_both_friend(host_id, guest_id):
            raise NotFriend

        key = UserPutAPIService.get_key_from_data(request.data)
        set_status = True if request.data[key] is "1" else False

        if FriendService.check_friend_status(host_id=host_id, guest_id=guest_id, key=key) is set_status:
            raise SameStatus

        FriendService.set_friend_status(host_id, guest_id, key, set_status)
        return Response(status=status.HTTP_200_OK)
