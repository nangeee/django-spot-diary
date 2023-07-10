from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name="comment")  # article.comment
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comment")  # article.comment
    content = models.TextField(null=False)
    created_time = models.DateTimeField(auto_now_add=True, null=False)

