from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy

from projectapp.models import Project


class ProjectCreationForm(ModelForm):

    class Meta:
        model = Project
        fields = ["title", "image", "description"]

        labels = {
            "title": gettext_lazy("Title"),
            "image": gettext_lazy("Image"),
            "description": gettext_lazy("Description")
        }

        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter the title of your project"}),
            "description": forms.Textarea(attrs={"placeholder": "Description about your project"})
        }

