from User.models import User, UserInform
from Profile.services import ProfileService


class KakaoIdService(object):
    @staticmethod
    def get_kakao_id_with_pk(pk: int) -> str:
        return ProfileService.get_profile_with_pk(pk).kakao_id

    @staticmethod
    def check_kakao_id_exist(kakao_id: str) -> bool:
        return True if len(UserInform.objects.filter(kakao_id=kakao_id).values()) else False

    @staticmethod
    def get_profile_with_kakao_id(kakao_id: str) -> UserInform:
        return UserInform.objects.get(kakao_id=kakao_id)

    @staticmethod
    def get_pk_with_kakao_id(kakao_id: str) -> int:
        return KakaoIdService.get_profile_with_kakao_id(kakao_id).user_id.id
