
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):  # django.forms.ModelForm
    class Meta:
        model = Profile
        fields = ["image", "nickname", "intro_msg"]
        widgets = {
            "intro_msg": forms.Textarea(attrs={"rows": 5, "placeholder": "Introduce yourself"}),
            "nickname": forms.TextInput(attrs={"placeholder": "Enter your nickname"}),
        }
        labels = {
            "intro_msg": gettext_lazy("Introduction"),
        }
        # help_texts = {
        #     "intro_msg": gettext_lazy("Introduce yourself"),
        # }


