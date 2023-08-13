from django import forms
from django.forms import ModelForm

from placeapp.models import Place


class PlaceSearchForm(forms.Form):
    searching_place = forms.CharField(label="",
                                      widget=forms.TextInput(attrs={"placeholder": "Search your place"}))


class PlaceCreationForm(ModelForm):
    class Meta:
        model = Place
        fields = ["name"]

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter the Place Name"}),
            "nickname": forms.TextInput(attrs={"placeholder": "Enter the address of your place"}),
        }

