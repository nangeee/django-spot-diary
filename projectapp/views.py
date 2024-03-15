from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscriptionapp.models import Subscription


# Create your views here.

@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "projectapp/create.html"

    def get_success_url(self):
        return reverse("projectapp:detail", kwargs={"pk": self.object.pk})


# MultipleObjectMixin: 여러 object를 다룰 수 있게 해줌
class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    template_name = "projectapp/detail.html"
    context_object_name = "current_project"

    # article에 project 필드 추가 -> MultipleObjectMixin 추가한 후
    paginate_by = 25

    # 현 project에 속한 article만 가져오도록 필터링하는 메서드
    # 템플릿에서 필터링된 object들 사용 가능
    def get_context_data(self, **kwargs):
        # 현재 user가 이 project를 구독하고 있는지 아닌지 판별해야 함
        project = self.object
        user = self.request.user

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)

        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                               subscription=subscription,
                                                               **kwargs)




class ProjectListView(ListView):
    model = Project
    template_name = "projectapp/list.html"
    context_object_name = "project_list"
    paginate_by = 25

