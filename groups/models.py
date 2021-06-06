from users.models import User
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=650)
    category = models.CharField(max_length=150)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="creator"
    )
    users_on_group = models.ManyToManyField(User)

    def __str__(self):
        return self.name
