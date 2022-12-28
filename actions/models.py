from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Priority(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=150)
    activeStatus = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return self.title


class Action(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    trackedTime = models.DurationField(null=True, blank=True)
    doneStatus = models.BooleanField(null=False, blank=False, default=False)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, blank=False)
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title
