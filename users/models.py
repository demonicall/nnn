from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name
