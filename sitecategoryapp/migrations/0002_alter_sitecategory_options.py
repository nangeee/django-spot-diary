# Generated by Django 4.1.5 on 2023-08-07 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sitecategoryapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="sitecategory",
            options={
                "verbose_name": "SiteCategory",
                "verbose_name_plural": "SiteCategories",
            },
        ),
    ]