"""
Registered Models for Actions App
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Action, Category, Priority, User

# Register your models here.
admin.site.register(Action)
admin.site.register(Category)
admin.site.register(Priority)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass

