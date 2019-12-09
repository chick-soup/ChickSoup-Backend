from django.contrib import admin
from .models import Friend


class FriendAdmin(admin.ModelAdmin):
    list_display = ['host_id', 'guest_id', 'bookmark', 'hidden', 'mute']


admin.site.register(Friend, FriendAdmin)
