import string
import random
from typing import List

from django.core.mail import send_mail
from django.template import loader
from django.utils.html import strip_tags

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
    def check_email_auth_ip(email: str) -> str:
        return EmailAuth.objects.get(email=email).auth_ip

    @staticmethod
    def create_email_queryset(email: str, auth_code: str) -> None:
        EmailAuth(email=email, auth_code=auth_code, auth_status=False).save()

    @staticmethod
    def delete_email_if_exist(email: str) -> None:
        if EmailService.check_email_exists(email):
            EmailAuth.objects.get(email=email).delete()

    @staticmethod
    def email_auth_complete(email: str, auth_ip: str) -> None:
        email_instance = EmailAuth.objects.get(email=email)
        email_instance.auth_status = True
        email_instance.auth_ip = auth_ip
        email_instance.save()

    @staticmethod
    def send_email(email: str, code: str) -> None:
        html_message = loader.render_to_string(
            'index.html',
            {
                'email': email,
                'code': code,
            }
        )

        send_mail(
            'ChickSoup 이메일 인증 코드입니다.',
            strip_tags(html_message),
            'richimous0719@gmail.com',
            [email],
            html_message=html_message
        )


class Random(object):
    @staticmethod
    def create_random_string(digit: int) -> str:
        result = ""
        for i in range(digit):
            result += random.choice(string.ascii_letters + string.digits)
        return result


class ClientService(object):
    @staticmethod
    def get_client_ip(request) -> str:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
