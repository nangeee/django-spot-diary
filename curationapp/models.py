from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Curation(models.Model):  # 하나의 큐레이션에 여러 개의 article을 담아서 소개 (1대다 관계)
    title = models.CharField(max_length=50, null=False)
    writer = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="writer")
    description = models.TextField()
    created_time = models.DateField(auto_now_add=True, null=False)


