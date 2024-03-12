from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.text import slugify

from curationapp.models import Curation
from placeapp.models import Place
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="article", null=True)
    # on_delete=models.SET_NULL -> user가 삭제되었을 때, article은 삭제되지 않고 user만 알 수 없음으로 바뀜
    # related_name="article" -> user.article로 접근 가능

    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name="article", null=True)

    title = models.CharField(max_length=200)
    # place = models.ForeignKey(Place, null=True, on_delete=models.SET_NULL, related_name="articles")
    image = models.ImageField(upload_to="article/", null=True, default=None)
    content = models.TextField()
    created_time = models.DateField(auto_now_add=True, null=False)

    # curation = models.ForeignKey(Curation, null=True, related_name="curation", on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Article"


def get_image_filename(instance, filename):
    # file will be uploaded to MEDIA_ROOT/article/<title>-<filename>
    title = instance.article.title
    slug = slugify(title, allow_unicode=True)  # django.template.defaultfilters.slugify
    return "article/%s-%s" % (slug, filename)


# class ArticleImage(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="image")
#
#     image = models.ImageField(upload_to=get_image_filename, null=True, default=None)
#
#     class Meta:
#         verbose_name = "Image"
#         verbose_name_plural = "Images"


