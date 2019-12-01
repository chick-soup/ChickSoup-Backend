from django.contrib import admin
from .models import (
    User, UserInform
)


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'password']


class UserInformAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'nickname', 'status_message']


admin.site.register(User, UserAdmin)
admin.site.register(UserInform, UserInformAdmin)
