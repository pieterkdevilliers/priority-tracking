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
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
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
    activeTrackedTime = models.DurationField(null=True, blank=True)
    trackedStart = models.DateTimeField(null=True, blank=True)
    trackedStop = models.DateTimeField(null=True, blank=True)
    doneStatus = models.BooleanField(null=False, blank=False, default=False)
    actionDate = models.DateField(auto_now_add=True)
    trackingStatus = models.BooleanField(null=False, blank=False, default=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="action", null=True)

    def __str__(self):
        return str(self.title)


class Report(models.Model):
    """
    Model for Reports - Used to track reporting per day.
    """
    reportDate = models.DateTimeField(auto_now_add=True)
    timeTrackedToday = models.DurationField(null=True, blank=True)
    actionsCompleted = models.IntegerField(null=True, blank=True)
    openActions = models.IntegerField(null=True, blank=True)
    percOnPriority = models.FloatField(null=True, blank=True)
    percOffPriority = models.FloatField(null=True, blank=True)
    timeOnPriority = models.DurationField(null=True, blank=True)
    timeOffPriority = models.DurationField(null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="report", null=True)

    def __str__(self):
        return str(self.reportDate)