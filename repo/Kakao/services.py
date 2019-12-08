from User.models import User, UserInform
from Profile.services import ProfileService


class KakaoIdService(object):
    @staticmethod
    def check_kakao_id_with_pk(pk: int) -> str:
        return ProfileService.get_profile_with_pk(pk).kakao_id
