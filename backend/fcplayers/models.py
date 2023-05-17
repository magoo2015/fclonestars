from django.db import models
from authentication.models import User

# Create your models here.

class Fcplayers(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
