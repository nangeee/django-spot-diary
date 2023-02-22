from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):  # django.forms.ModelForm
    class Meta:
        model = Profile
        fields = ["image", "nickname", "intro_msg"]

