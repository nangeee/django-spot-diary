from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscriptionapp.models import Subscription


# Create your views here.


# 구독 기능: form 입력, detail 화면 등이 필요없음
# RedirectView 상속
@method_decorator(login_required, "get")
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        # project detail view에서 구독 버튼 누르도록 할 것
        # project detail view에서 get 방식으로 project_pk를 넘겨줌 -> 해당 project의 detail view로 redirect되도록
        return reverse("projectapp:detail", kwargs={"pk": self.request.GET.get("project_pk")})

    def get(self, request, *args, **kwargs):
        # 현재 user가 subscribe한 project만 찾아와야 함

        # pk가 project_pk인 Project를 찾는데, 만약 해당 object가 없다면 404를 return
        project = get_object_or_404(Project, pk=self.request.GET.get("project_pk"))
        user = self.request.user

        subscription = Subscription.objects.filter(user=user, project=project)

        # toggle 형식: 구독했으면 -> 구독 취소, 구독 아직 안 했으면 -> 구독
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()


        return super(SubscriptionView, self).get(request, *args, **kwargs)


method_decorator(login_required, "get")
class SubscriptionListView(ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "subscriptionapp/list.html"
    paginate_by = 5

    def get_queryset(self):
        # 1) user가 구독한 project 모두 가져오기
        # values_list: 값들을 가져와서 리스트화
        # Subscription object를 모두 가져와서 그 중 project field만 모두 리스트로 가져오기
        projects = Subscription.objects.filter(user=self.request.user).values_list("project")

        # 2) user가 구독한 project 내의 article 모두 가져오기
        # Field Lookup
        # "project__in" == select ... where project in ...
        article_list = Article.objects.filter(project__in=projects)

        return article_list
