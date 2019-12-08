from django.db import models
from User.models import User


class Friend(models.Model):
    host_id = models.IntegerField()
    guest_id = models.IntegerField()
    bookmark = models.BooleanField(default=False)
    hidden = models.BooleanField(default=False)
    mute = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.host_id} -> {self.guest_id}"
