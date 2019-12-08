from User.models import User, UserInform
from User.services import UserService


class ProfileService(object):
    @staticmethod
    def get_profile_with_pk(pk: int) -> UserInform:
        return UserInform.objects.get(user_id=UserService.get_user_by_pk(pk))

    @staticmethod
    def change_profile_with_pk(pk: int, nickname: str, status_message: str) -> None:
        profile = UserInform.objects.get(user_id=UserService.get_user_by_pk(pk))
        profile.nickname = nickname
        profile.status_message = status_message
        profile.save()
