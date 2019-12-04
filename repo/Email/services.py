import string
import random
from typing import List

from django.core.mail import send_mail

from .models import EmailAuth


class EmailService(object):
    @staticmethod
    def check_email_exists(email: str) -> bool:
        return True if len(EmailAuth.objects.filter(email=email).values()) else False

    @staticmethod
    def check_email_auth_status(email: str) -> bool:
        return EmailAuth.objects.get(email=email).auth_status

    @staticmethod
    def check_email_auth_code(email: str) -> str:
        return EmailAuth.objects.get(email=email).auth_code

    @staticmethod
    def create_email_queryset(email: str, auth_code: str) -> None:
        EmailAuth(email=email, auth_code=auth_code, auth_status=False).save()

    @staticmethod
    def delete_email_if_exist(email: str) -> None:
        if EmailService.check_email_exists(email):
            EmailAuth.objects.get(email=email).delete()

    @staticmethod
    def email_auth_complete(email: str) -> None:
        email_instance = EmailAuth.objects.get(email=email)
        email_instance.auth_status = True
        email_instance.save()

    @staticmethod
    def send_email(*email_list: List[str, ], code: str) -> None:
        for email in email_list:
            send_mail(
                'ChickSoup 이메일 인증 코드입니다.',
                f"""
                If you want to go through the certification process for our service, you need to read this article.

                Hello, customer with e-mail {email}?
                Thank you very much for your email certification to use our service.
                The authentication number for your email we provided is {code}.
                """,
                'richimous0719@gmail.com',
                [email],
                fail_silently=False,
            )


class Random(object):
    @staticmethod
    def create_random_string(digit: int) -> str:
        result = ""
        for i in range(digit):
            result += random.choice(string.ascii_letters + string.digits)
        return result
