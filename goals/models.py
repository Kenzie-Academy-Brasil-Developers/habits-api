from django.db import models
from groups.models import Group


class Goal(models.Model):
    title = models.CharField(max_length=150)
    difficulty = models.CharField(max_length=150)
    achieved = models.BooleanField(default=False)
    how_much_achieved = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="goals")

    def __str__(self):
        return self.title