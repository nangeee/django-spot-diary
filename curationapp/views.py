from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from curationapp.forms import CurationCreationForm
from curationapp.models import Curation


class CurationCreateView(CreateView):
    model = Curation
    form_class = CurationCreationForm
    # success_url = reverse_lazy("curationapp:detail", kwargs={"pk":})
    template_name = "curationapp/create.html"


class CurationListView(ListView):
    model = Curation
    context_object_name = "curation_list"
    template_name = "curationapp/list.html"

