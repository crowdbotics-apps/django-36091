from django.conf import settings
from django.db import models


class User1(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=200,
    )
    email = models.EmailField(
        max_length=254,
    )
    password = models.CharField(
        max_length=200,
    )
    age = models.BigIntegerField()
