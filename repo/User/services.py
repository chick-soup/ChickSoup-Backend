import bcrypt
import jwt
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

from conf.hidden import JWT_SECRET_KEY


class UserService(object):
    @staticmethod
    def check_email_exists(email: str) -> bool:
        return True if len(User.objects.filter(email=email).values()) else False

    @staticmethod
    def check_pk_exists(pk: int) -> bool:
        return True if len(User.objects.filter(pk=pk).values()) else False

    @staticmethod
    def create_new_user(email: str, hashed_password: str) -> int:
        user = User(email=email, password=hashed_password)
        user.save()
        UserInform(user_id=user, nickname="DEFAULT", status_message=None).save()

        return user.id


class HashService(object):
    @staticmethod
    def hash_string_to_password(password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


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


print(JWTService.create_access_token_with_id(1))
