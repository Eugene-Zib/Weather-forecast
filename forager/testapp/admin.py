"""This id test task."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Users

admin.site.register(Users, UserAdmin)
admin.site.register(User)
