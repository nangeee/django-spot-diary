from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

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