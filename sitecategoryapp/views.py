from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.

# 카테고리 create는 admin에서만 가능하도록 -> create view, delete view, update view는 생성 x
# list view, detail view만 생성
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from sitecategoryapp.models import SiteCategory, ChildCategory


@method_decorator(login_required, "get")
class SiteCategoryListView(ListView):
    model = SiteCategory
    context_object_name = "sitecategory_list"
    template_name = "sitecategoryapp/list.html"


class SiteCategoryDetailView(LoginRequiredMixin, DetailView):
    model = ChildCategory
    context_object_name = "current_category"
    template_name = "sitecategoryapp/detail.html"
