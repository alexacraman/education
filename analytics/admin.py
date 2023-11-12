from django.contrib import admin

from .models import UserSession

# admin.site.register(ObjectViewed)


class UserModelAdmin(admin.ModelAdmin):
    ordering = ['timestamp']
    list_display = ['user', 'ip_address', 'session_key', 'timestamp','loggedout', 'ended', 'total']

admin.site.register(UserSession, UserModelAdmin)
