from django.urls import path

from placeapp.views import create_profile, PlaceListView

app_name = "placeapp"

urlpatterns = [
    path("create/", create_profile, name="create"),
    path("list/", PlaceListView.as_view(), name="list"),
    # path("detail/<int:pk>", PlaceDetailView.as_view(), name="detail"),
]
