from django.db import models


class User(models.Model):
    class Meta:
        verbose_name_plural = 'User'
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=30)
    password = models.TextField()

    def __str__(self):
        return self.email


class UserInform(models.Model):
    class Meta:
        verbose_name_plural = "UserInform"
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    kakao_id = models.CharField(max_length=10, default='DEFAULT_KAKAO_ID')
    nickname = models.CharField(max_length=16)
    status_message = models.CharField(max_length=100, null=True)
