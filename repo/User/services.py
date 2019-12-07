import bcrypt
import jwt
import boto3
from datetime import datetime, timedelta

from .models import (
    User,
    UserInform
)
from .exceptions import (
    NoIncludeJWT,
    IncorrectJWT,
    ExpiredJWT
)
from Email.services import Random
from conf.hidden import JWT_SECRET_KEY, MY_AWS_ACCESS_KEY_ID, MY_AWS_SECRET_ACCESS_KEY, MY_AWS_REGION


class UserService(object):
    @staticmethod
    def check_email_exists(email: str) -> bool:
        return True if len(User.objects.filter(email=email).values()) else False

    @staticmethod
    def check_pk_exists(pk: int) -> bool:
        return True if len(User.objects.filter(pk=pk).values()) else False

    @staticmethod
    def get_user_by_email(email: str) -> User:
        return User.objects.get(email=email)

    @staticmethod
    def create_new_user(email: str, hashed_password: str) -> int:
        user = User(email=email, password=hashed_password)
        user.save()
        UserInform(user_id=user, kakao_id=KakaoIdService.create_new_kakao_id(), nickname="DEFAULT", status_message=None).save()

        return user.id

    @staticmethod
    def update_user_profile(pk: int, nickname: str, status_message: str = None) -> None:
        user = UserInform.objects.get(user_id=User.objects.get(pk=pk))
        user.nickname = nickname
        user.status_message = status_message
        user.save()


class HashService(object):
    @staticmethod
    def hash_string_to_password(password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def compare_pw_and_hash(password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))


class KakaoIdService(object):
    @staticmethod
    def create_new_kakao_id() -> str:
        kakao_id_list = []
        for user in list(UserInform.objects.all().values()):
            kakao_id_list.append(user["kakao_id"])

        while True:
            random = Random.create_random_string(16)
            if random not in kakao_id_list:
                return random


class JWTService(object):
    @staticmethod
    def run_auth_process(headers: dict) -> int:
        try:
            pk = JWTService.decode_access_token_to_id(headers['Authorization'])
        except KeyError:
            raise NoIncludeJWT
        except jwt.exceptions.InvalidSignatureError:
            raise IncorrectJWT
        except jwt.exceptions.ExpiredSignatureError:
            raise ExpiredJWT

        return pk

    @staticmethod
    def create_access_token_with_id(user_id: int, expired_minute: int = 60) -> str:
        return jwt.encode({
            'id': user_id,
            'exp': datetime.utcnow()+timedelta(minutes=expired_minute)
        }, JWT_SECRET_KEY, algorithm='HS256', headers={
            'token': 'access'
        })

    @staticmethod
    def decode_access_token_to_id(access_token: str) -> int:
        if not jwt.get_unverified_header(access_token)['token'] == 'access':
            raise IncorrectJWT
        return jwt.decode(access_token, JWT_SECRET_KEY, algorithms=['HS256'])['id']


class S3Service(object):
    @staticmethod
    def make_s3_resource():
        s3_resource = boto3.resource(
            's3',
            aws_access_key_id=MY_AWS_ACCESS_KEY_ID,
            aws_secret_access_key=MY_AWS_SECRET_ACCESS_KEY,
            region_name=MY_AWS_REGION,
        )

        return s3_resource
