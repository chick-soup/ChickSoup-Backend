from django.contrib import admin
from .models import (
    EmailAuth
)


class EmailAuthAdmin(admin.ModelAdmin):
    list_display = ['email', 'auth_code', 'auth_status', 'auth_ip']


admin.site.register(EmailAuth, EmailAuthAdmin)
