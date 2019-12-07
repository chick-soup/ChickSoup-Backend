from User.models import User, UserInform
from User.services import UserService


class ProfileService(object):
    @staticmethod
    def get_profile_with_pk(pk):
        return UserInform.objects.get(user_id=UserService.get_user_by_pk(pk))
