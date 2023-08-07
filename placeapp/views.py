from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from placeapp.forms import PlaceCreationForm
from placeapp.models import Place
from sitecategoryapp.models import SiteCategory


def create_profile(request):
    if request.method == "POST":
        place_form = PlaceCreationForm(request.POST)

    else:
        place_form = PlaceCreationForm()
        parent_categories = SiteCategory.objects.all()

        return render(request, template_name="placeapp/create.html",
                        context={"form": place_form, "parent_categories": parent_categories})



class PlaceCreateView(CreateView):
    model = Place
    template_name = "placeapp/create.html"
    # success_url = reverse_lazy("placeapp:detail", kwargs={"pk":})
    form_class = PlaceCreationForm


class PlaceListView(ListView):
    model = Place