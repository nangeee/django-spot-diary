from django.contrib import admin

# Register your models here.
from sitecategoryapp.models import SiteCategory, ChildCategory

admin.site.register(SiteCategory)
admin.site.register(ChildCategory)
