from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import User as myUser


# Function Based View
def helloWorld(request):
    if request.method == "POST":

        user = myUser() # models.py의 User 클래스 객체 생성
        user.userName = request.POST.get("userName") # post 방식으로 받은 데이터 중에서, userName 이라는 이름의 데이터 가져오기
        user.userID = request.POST.get("userID")
        user.password = request.POST.get("password")
        user.save() # 만든 객체 저장 -> 실제 DB에 저장됨

        # users = User.objects.all()

        # return render(request, template_name="accountapp/helloWorld.html",
        #               context={"userInfo": user, "usersInfo": users})
        return HttpResponseRedirect(reverse("accountapp:helloWorld"))
    else:
        users = myUser.objects.all()
        return render(request, template_name="accountapp/helloWorld.html",
                      context={"usersInfo": users})

    # return render(request, template_name="accountapp/helloWorld.html")
    # return HttpResponse("Hello, World!") # Alt + Enter로 라이브러리 import 가능



# Class Based View로 Account Creation View 생성
class AccountCreateView(CreateView):  # django.views.generic.CreateView
    # 무슨 모델을 사용? -> 장고 기본 제공 User
    model = User  # django.contrib.auth.models.User -> ctrl + B 로 소스코드 확인

    # user model을 만들 때 사용할 form 필요
    form_class = UserCreationForm  # django.contrib.auth.forms.UserCreationForm

    # account creation 성공했을 때 -> 어느 경로로 재연결할지 지정
    success_url = reverse_lazy("accountapp:helloWorld")  # Function Based View에서는 reverse 함수 사용
    # Function과 Class 내부 방식의 차이 때문에 Class Based View에서는 reverse가 아닌 reverse_lazy 사용해야 함

    # account creation 과정에서 볼 html view 지정
    template_name = "accountapp/createAccount.html"


class AccountDetailView(DetailView):  # django.views.generic.DetailView
    model = User
    context_object_name = "current_user"
    template_name = "accountapp/detail.html"


# Account 정보 수정 -> AccountUpdateView
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy("accountapp:helloWorld")
    template_name = "accountapp/update.html"


# Account 삭제 -> AccountDeleteView
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("accountapp:helloWorld")
    template_name = "accountapp/delete.html"

    