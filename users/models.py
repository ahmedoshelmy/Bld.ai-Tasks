from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.CharField(max_length=256, default='')

    class Meta:
        db_table = 'my_user'
