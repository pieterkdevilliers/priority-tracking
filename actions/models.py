'''
All models for the Actions App
'''

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    """
    Model for Categories - Used to group Actions within Categories.
    """
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=150)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="categories", null=True)

    def __str__(self):
        return str(self.title)


class Priority(models.Model):
    """
    Model for Priorities - Used to assign Actions to Priorities.
    """
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=150)
    activeStatus = models.BooleanField(null=False, blank=False, default=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="priorities", null=True)

    def __str__(self):
        return str(self.title)


class Action(models.Model):
    """
    Model for Actions - Used to track Actions.
    """
    title = models.CharField(max_length=50, null=False, blank=False)
    trackedTime = models.DurationField(null=True, blank=True)
    doneStatus = models.BooleanField(null=False, blank=False, default=False)
    actionDate = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, blank=False)
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="action", null=True)

    def __str__(self):
        return str(self.title)


