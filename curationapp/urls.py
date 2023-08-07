from django.urls import path

from curationapp.views import CurationCreateView, CurationListView

app_name = "curationapp"

urlpatterns = [
    path("create/", CurationCreateView.as_view(), name="create"),
    path("list/", CurationListView.as_view(), name="list"),
]