from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscription")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="subscription")

    # 하나의 project(게시판)을 '한 번만' 구독할 수 있음. 여러 번 중복 구독 불가.
    class Meta:
        # user - project 구독 pair는 하나만 존재할 수 있도록 함
        unique_together = ("user", "project")
