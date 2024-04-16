from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    class Meta:
        db_table = "user"
        # ordering =

    def __str__(self):
        # return f'{self.last_name} {self.first_name}'
        return f'{self.username}'
