from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=650)
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.name