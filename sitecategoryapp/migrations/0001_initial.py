# Generated by Django 4.1.5 on 2023-08-06 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SiteCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
            ],
            options={
                "verbose_name": "SiteCategory",
            },
        ),
        migrations.CreateModel(
            name="ChildCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("image", models.ImageField(upload_to="childcategory")),
                (
                    "parent_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="childcategory",
                        to="sitecategoryapp.sitecategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "ChildCategory",
                "verbose_name_plural": "ChildCategories",
            },
        ),
    ]
