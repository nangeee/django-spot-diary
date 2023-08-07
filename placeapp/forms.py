from django import forms
from django.forms import ModelForm

from placeapp.models import Place


class PlaceCreationForm(ModelForm):
    class Meta:
        model = Place
        fields = ["name", "address"]

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter the Place Name"}),
            "nickname": forms.TextInput(attrs={"placeholder": "Enter the address of your place"}),
        }