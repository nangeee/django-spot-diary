from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import create_article, ArticleDetailView

app_name = "articleapp"

urlpatterns = [
    path("list/", TemplateView.as_view(template_name="articleapp/list.html"), name="list"),
    path("create/", create_article, name="create"),
    path("detail/<int:pk>", ArticleDetailView.as_view(template_name="articleapp/detail.html"), name="detail"),
    # path("detail/<int:pk>", ArticleDetailView.as_view(template_name="articleapp/detail.html"), name="detail"),
]

