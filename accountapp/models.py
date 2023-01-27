from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=20, null=False)
    userID = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=25, null=False)


