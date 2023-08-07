from django.forms import ModelForm

from curationapp.models import Curation


class CurationCreationForm(ModelForm):
    class Meta:
        model = Curation

        fields = ["title", "description"]

