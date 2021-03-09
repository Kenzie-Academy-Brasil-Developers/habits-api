from django.db import models
from users.models import User


class Habit(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    difficulty = models.CharField(max_length=150)
    frequency = models.CharField(max_length=150)
    achieved = models.BooleanField(default=False)
    how_much_achieved = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
