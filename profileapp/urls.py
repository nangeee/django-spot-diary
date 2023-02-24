from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = "profileapp"

urlpatterns = [
    path("createProfile/", ProfileCreateView.as_view(), name="createProfile"),
    path("updateProfile/<int:pk>", ProfileUpdateView.as_view(), name="update"),
]


