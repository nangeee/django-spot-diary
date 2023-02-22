from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # related_name="profile" -> user.profile.image와 같이 접근 가능

    image = models.ImageField(upload_to="profile/", null=True)

    nickname = models.CharField(max_length=25, unique=True)

    intro_msg = models.TextField(null=True)


