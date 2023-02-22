from django.urls import path

from profileapp.views import ProfileCreateView

app_name = "profileapp"

urlpatterns = [
    path("createProfile/", ProfileCreateView.as_view(), name="createProfile")
]
