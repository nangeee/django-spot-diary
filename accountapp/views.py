from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

from accountapp.models import User


def helloWorld(request):
    if request.method == "POST":

        user = User() # models.py의 User 클래스 객체 생성
        user.userName = request.POST.get("userName") # post 방식으로 받은 데이터 중에서, userName 이라는 이름의 데이터 가져오기
        user.userID = request.POST.get("userID")
        user.password = request.POST.get("password")
        user.save() # 만든 객체 저장 -> 실제 DB에 저장됨

        # users = User.objects.all()

        # return render(request, template_name="accountapp/helloWorld.html",
        #               context={"userInfo": user, "usersInfo": users})
        return HttpResponseRedirect(reverse("accountapp:helloWorld"))
    else:
        users = User.objects.all()
        return render(request, template_name="accountapp/helloWorld.html",
                      context={"usersInfo": users})

    # return render(request, template_name="accountapp/helloWorld.html")
    # return HttpResponse("Hello, World!") # Alt + Enter로 라이브러리 import 가능

