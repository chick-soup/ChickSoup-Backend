from django.core.mail import send_mail

from .models import EmailAuth


class EmailService(object):
    @staticmethod
    def check_email_exists(email):
        return True if len(EmailAuth.objects.filter(email=email).values()) else False

    @staticmethod
    def check_email_auth_status(email):
        return EmailAuth.objects.get(email=email).auth_status

    @staticmethod
    def delete_email_if_exist(email):
        if EmailService.check_email_exists(email):
            EmailAuth.objects.get(email=email).delete()

    @staticmethod
    def send_email(*email_list, code):
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

