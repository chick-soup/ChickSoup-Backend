from django.db import models

from django.db.models import *
from User.models import User

class FriendsList(Model):
    class Meta:
        verbose_name_plural = "Friendslist"

    host_id = ForeignKey(User, on_delete=CASCADE, related_name='host_id')

    guest_id = ForeignKey(User, on_delete=CASCADE, related_name='guest_id')

    bookmark = BooleanField(null=True)

    hidden = BooleanField(null=True)

    mute = BooleanField(null=True)