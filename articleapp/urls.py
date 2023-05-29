from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import create_article, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

app_name = "articleapp"

urlpatterns = [
    path("list/", TemplateView.as_view(template_name="articleapp/list.html"), name="list"),
    path("create/", create_article, name="create"),
    path("detail/<int:pk>", ArticleDetailView.as_view(template_name="articleapp/detail.html"), name="detail"),
    # path("update/<int:pk>", ArticleUpdateView.as_view(template_name="articleapp/update.html"), name="update"),
    path("update/<int:pk>", ArticleUpdateView, name="update"),
    path("delete/<int:pk>", ArticleDeleteView.as_view(template_name="articleapp/delete.html"), name="delete"),
    # path("detail/<int:pk>", ArticleDetailView.as_view(template_name="articleapp/detail.html"), name="detail"),
]

