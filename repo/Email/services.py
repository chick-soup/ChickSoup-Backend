from django.core.mail import send_mail

from .models import EmailAuth


class EmailService(object):
    @staticmethod
    def check_email_exists(email):
        return True if len(EmailAuth.objects.filter(email=email).values()) else False

    @staticmethod
    def check_email_auth_status(email):
        print(1)
        return EmailAuth.objects.get(email=email).auth_status

    @staticmethod
    def send_email(*email):
        send_mail(
            'Subject',
            'Message',
            'richimous0719@gmail.com',
            email,
            fail_silently=False,
        )
