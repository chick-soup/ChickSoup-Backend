from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .services import (
    ProfileService
)
from User.services import (
    JWTService,
    UserService
)
from User.exceptions import UserNotFound


class MyProfileAPI(APIView):
    def get(self, request):
        pk = JWTService.run_auth_process(request.headers)

        if not UserService.check_pk_exists(pk):
            raise UserNotFound

        my_profile = ProfileService.get_profile_with_pk(pk)

        return Response({
            "id": pk,
            "nickname": my_profile.nickname,
            "status_message": "" if my_profile.status_message is None else my_profile.status_message
        }, status=status.HTTP_200_OK)
