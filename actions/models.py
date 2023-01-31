'''
All models for the Actions App
'''
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Category(models.Model):
    """
    Model for Categories - Used to group Actions within Categories.
    """
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=150)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="categories", null=True)

    def __str__(self):
        return str(self.title)


class Priority(models.Model):
    """
    Model for Priorities - Used to assign Actions to Priorities.
    """
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=150)
    activeStatus = models.BooleanField(null=False, blank=False, default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="priorities", null=True)
    

    def __str__(self):
        return str(self.title)


class Action(models.Model):
    """
    Model for Actions - Used to track Actions.
    """
    title = models.CharField(max_length=50, null=False, blank=False)
    tracked_time = models.DurationField(null=True, blank=True)
    active_tracked_time = models.DurationField(null=True, blank=True)
    tracked_start = models.DateTimeField(null=True, blank=True)
    tracked_stop = models.DateTimeField(null=True, blank=True)
    done_status = models.BooleanField(null=False, blank=False, default=False)
    action_date = models.DateField(auto_now_add=True)
    tracking_status = models.BooleanField(null=False, blank=False, default=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'activetatus': True})
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="action", null=True)

    def __str__(self):
        return str(self.title)

class User(AbstractUser):
    email = models.EmailField(unique=True)
