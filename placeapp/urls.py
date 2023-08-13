from django.urls import path

from placeapp.views import PlaceListView, create_place, PlaceDetailView, search_place

app_name = "placeapp"

urlpatterns = [
    path("create/", create_place, name="create"),
    path("list/", PlaceListView.as_view(), name="list"),
    path("detail/<int:pk>", PlaceDetailView.as_view(), name="detail"),
    path("search/", search_place, name="search")
]
