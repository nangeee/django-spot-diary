from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from sitecategoryapp.models import ChildCategory


class Place(models.Model):
    name = models.CharField(max_length=30, null=False)
    first_discoverer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="place")
    address = models.CharField(max_length=100, null=False)
    category = models.ManyToManyField(ChildCategory, related_name="places")  # 다대다 관계
