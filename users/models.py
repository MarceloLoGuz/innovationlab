from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class MyAbsUser(AbstractUser):
    name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=13, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)


    def save(self, *args, **kwargs):
        if not self.username:
            self.username = str(uuid.uuid4())

        super().save(*args, **kwargs)


    def __str__(self):
        return self.pk