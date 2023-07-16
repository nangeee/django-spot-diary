from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name="comment")  # article.comment
    # article도 서버 단에서 받아서 작업 -> create.html의 hidden input

    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comment")  # article.comment
    content = models.TextField(null=False)
    created_time = models.DateTimeField(auto_now_add=True, null=False)

