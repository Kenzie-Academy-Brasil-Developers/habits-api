from django.db import models
from django.contrib.auth.models import AbstractUser
from groups.models import Group


class User(AbstractUser):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name="users")

    def __str__(self):
        return self.username
