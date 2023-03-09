from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="article", null=True)
    # on_delete=models.SET_NULL -> user가 삭제되었을 때, article은 삭제되지 않고 user만 알 수 없음으로 바뀜
    # related_name="article" -> user.article로 접근 가능

    title = models.CharField(max_length=200)
    place_name = models.CharField(max_length=100, null=False) # 장소 이름 (식당 이름, 서점 이름 등)
    address = models.CharField(max_length=300)
    # image = models.ImageField(upload_to="article/", null=False)
    content = models.TextField()
    created_time = models.DateField(auto_now_add=True, null=False)

    class Meta:
        verbose_name = "Article"


def get_image_filename(instance, filename):
    # file will be uploaded to MEDIA_ROOT/article/<title>-<filename>
    title = instance.article.title
    slug = slugify(title, allow_unicode=True)  # django.template.defaultfilters.slugify
    return "article/%s-%s" % (slug, filename)


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="image")

    image = models.ImageField(upload_to=get_image_filename, null=True, default=None)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


