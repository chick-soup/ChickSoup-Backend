import bcrypt

from .models import User


class UserService(object):
    @staticmethod
    def check_email_exists(email: str) -> bool:
        return True if len(User.objects.filter(email=email).values()) else False


class HashService(object):
    @staticmethod
    def hash_string_to_password(password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
