from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def helloWorld(request):
    return render(request, template_name="accountapp/helloWorld.html")

    # return HttpResponse("Hello, World!") # Alt + Enter로 라이브러리 import 가능

