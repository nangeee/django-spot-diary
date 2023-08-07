from django.db import models

# Create your models here.


class SiteCategory(models.Model):
    name = models.CharField(max_length=20, null=False)  # 카테고리명 (식음료, 여행, 문화, 쇼핑 등)

    class Meta:
        verbose_name = "SiteCategory"
        verbose_name_plural = "SiteCategories"


class ChildCategory(models.Model):
    name = models.CharField(max_length=20, null=False)  # 세부 카테고리명 (카페, 바, 관광, 운동, 쇼핑몰 등)
    image = models.ImageField(upload_to="childcategory", null=False)
    parent_category = models.ForeignKey(SiteCategory, on_delete=models.CASCADE, related_name="childcategory")

    class Meta:
        verbose_name = "ChildCategory"
        verbose_name_plural = "ChildCategories"
