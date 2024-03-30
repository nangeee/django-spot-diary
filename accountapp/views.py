from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm, UserCreationForm2, LoginForm2
# from accountapp.forms import AccountUpdateForm
from accountapp.models import User as myUser
from articleapp.models import Article

ownership_authenticated = [
    account_ownership_required,
    login_required
]



# Class Based View로 Account Creation View 생성
class AccountCreateView(CreateView):  # django.views.generic.CreateView
    # 무슨 모델을 사용? -> 장고 기본 제공 User
    model = User  # django.contrib.auth.models.User -> ctrl + B 로 소스코드 확인

    # user model을 만들 때 사용할 form 필요
    # form_class = UserCreationForm  # django.contrib.auth.forms.UserCreationForm
    form_class = UserCreationForm2  # accountapp.forms.UserCreationForm2

    # account creation 성공했을 때 -> 어느 경로로 재연결할지 지정
    success_url = reverse_lazy("home")  # Function Based View에서는 reverse 함수 사용
    # Function과 Class 내부 방식의 차이 때문에 Class Based View에서는 reverse가 아닌 reverse_lazy 사용해야 함

    # account creation 과정에서 볼 html view 지정
    template_name = "accountapp/createAccount.html"


# Class Based View에서 login required 데코레이터 사용하려면
# 첫 번째 인자로 LoginRequiredMixin 전달
# 또는 method_decorator를 get 함수에만 적용 (DetailView에는 get 메서드만 존재함)
@method_decorator(account_ownership_required, "get")
class AccountDetailView(LoginRequiredMixin, DetailView, MultipleObjectMixin):  # django.views.generic.DetailView
    model = User
    context_object_name = "current_user"
    template_name = "accountapp/detail.html"

    # MultipleObjectMixin 적용 후
    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


# Account 정보 수정 -> AccountUpdateView
@method_decorator(ownership_authenticated, "get")
@method_decorator(ownership_authenticated, "post")
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = "current_user"
    form_class = AccountUpdateForm
    success_url = reverse_lazy("home")
    template_name = "accountapp/update.html"


# Account 삭제 -> AccountDeleteView
@method_decorator(ownership_authenticated, "get")
@method_decorator(ownership_authenticated, "post")
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = "current_user"
    success_url = reverse_lazy("home")
    template_name = "accountapp/delete.html"


class CustomizedLoginView(LoginView):
    form_class = LoginForm2
    template_name = "accountapp/login.html"


