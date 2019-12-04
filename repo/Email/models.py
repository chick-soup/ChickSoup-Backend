from django.db import models


class EmailAuth(models.Model):
    class Meta:
        verbose_name_plural = 'EmailAuth'
    email = models.CharField(max_length=30)
    auth_code = models.CharField(max_length=10)
    auth_status = models.BooleanField()
    auth_ip = models.CharField(max_length=20, default="127.0.0.1")

    def __str__(self):
        return self.email
