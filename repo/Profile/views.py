from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .services import (
    ProfileService
)
from .serializers import (
    MyProfilePutSerializer
)
from User.services import (
    JWTService,
    UserService,
    S3Service
)
from User.exceptions import UserNotFound


class MyProfileAPI(APIView):
    def get(self, request):
        pk = JWTService.run_auth_process(request.headers)

        if not UserService.check_pk_exists(pk):
            raise UserNotFound

        profile = ProfileService.get_profile_with_pk(pk)

        return Response({
            "id": pk,
            "nickname": profile.nickname,
            "status_message": "" if profile.status_message is None else profile.status_message
        }, status=status.HTTP_200_OK)

    def put(self, request):
        pk = JWTService.run_auth_process(request.headers)

        serializer = MyProfilePutSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if not UserService.check_pk_exists(pk):
            raise UserNotFound

        profile = request.FILES.get('profile')
        if profile is not None:
            S3Service.upload_profile(pk, profile, S3Service.make_s3_resource())

        data = serializer.initial_data
        ProfileService.change_profile_with_pk(pk, data["nickname"], data["status_message"])
        return Response(status=status.HTTP_200_OK)


class PkProfileAPI(APIView):
    def get(self, request, user_id):
        pk = JWTService.run_auth_process(request.headers)

        if not (UserService.check_pk_exists(pk) and UserService.check_pk_exists(user_id)):
            raise UserNotFound

        profile = ProfileService.get_profile_with_pk(user_id)

        # 친구 API 구현 후 해당 user_id가 친구가 아니면 exception 추가 하기

        return Response({
            "id": user_id,
            "nickname": profile.nickname,
            "status_message": "" if profile.status_message is None else profile.status_message,
            "myself": True if pk is user_id else False
        }, status=status.HTTP_200_OK)

