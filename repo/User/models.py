from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=30)
    password = models.TextField()

    def __str__(self):
        return self.email


class UserInform(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=12)
    status_message = models.CharField(max_length=100)
