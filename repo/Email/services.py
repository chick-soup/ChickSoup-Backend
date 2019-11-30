from .models import EmailAuth


class EmailService(object):
    @staticmethod
    def check_email_exists(email):
        return False if len(EmailAuth.objects.filter(email=email).values()) else True
