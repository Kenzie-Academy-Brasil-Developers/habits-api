from django.db import models
from groups.models import Group


class Activity(models.Model):
    title = models.CharField(max_length=150)
    realization_time = models.DateTimeField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="activities")

    def __str__(self):
        return self.title