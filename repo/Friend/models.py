from django.db import models

from django.db.models import *
from User.models import User

class FriendsList(Model):
    class Meta:
        verbose_name_plural = "Friendslist"

    host_id = ForeignKey(User, on_delete=CASCADE)

    guest_id = ForeignKey(User, on_delete=CASCADE)

    bookmark = BooleanField()

    hidden = BooleanField()

    mute = BooleanField()