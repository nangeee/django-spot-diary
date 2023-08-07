from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView
from sitecategoryapp.views import SiteCategoryListView, SiteCategoryDetailView

app_name = "sitecategoryapp"

urlpatterns = [
    path("list/", SiteCategoryListView.as_view(), name="list"),
    path("detail/<int:pk>", SiteCategoryDetailView.as_view(), name="detail"),
]