from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=150, unique=True, null=True)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name

