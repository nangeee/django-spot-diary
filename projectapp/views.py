from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

from projectapp.forms import ProjectCreationForm
from projectapp.models import Project


# Create your views here.

@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "projectapp/create.html"

    def get_success_url(self):
        return reverse("projectapp:detail", kwargs={"pk": self.object.pk})


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projectapp/detail.html"
    context_object_name = "current_project"


class ProjectListView(ListView):
    model = Project
    template_name = "projectapp/list.html"
    context_object_name = "project_list"
    paginate_by = 25

