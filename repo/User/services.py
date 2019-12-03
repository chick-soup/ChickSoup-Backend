import bcrypt
import jwt
from datetime import datetime, timedelta

from .models import (
    User,
    UserInform
)

from conf.hidden import JWT_SECRET_KEY


class UserService(object):
    @staticmethod
    def check_email_exists(email: str) -> bool:
        return True if len(User.objects.filter(email=email).values()) else False

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
    def create_access_token_with_id(user_id: int, expired_minute: int = 60) -> str:
        return jwt.encode({
            'id': user_id,
            'exp': datetime.utcnow()+timedelta(minutes=expired_minute)
        }, JWT_SECRET_KEY, algorithm='HS256', headers={
            'token': 'access'
        })

