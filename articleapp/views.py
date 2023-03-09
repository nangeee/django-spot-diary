from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator

from articleapp.decorators import account_ownership_required
from articleapp.forms import *
from articleapp.models import *


@login_required
@account_ownership_required
def create_article(request):
    # 하나의 modelform 을 여러번 쓸 수 있음. 모델, 모델폼, 몇 개의 폼을 띄울건지 갯수
    ImageFormSet = modelformset_factory(ArticleImage, form=ArticleImageForm, extra=5)

    if request.method == "POST":
        ArticleForm = ArticleCreationForm(request.POST)
        # queryset 을 none 으로 정의해서 이미지가 없어도 되도록 설정. none 은 빈 쿼리셋 리턴
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=ArticleImage.objects.none())

        if ArticleForm.is_valid() and formset.is_valid():
            # article 저장을 잠시 멈추고
            complete_ArticleForm = ArticleForm.save(commit=False)

            # article의 writer를 현재 로그인한 user로
            complete_ArticleForm.writer = request.user

            complete_ArticleForm.save()

            for img_from_form in formset.cleaned_data:
                # ArticleImageForm에 입력된 이미지 하나하나 저장
                if img_from_form:
                    image_file = img_from_form["image"]
                    # 뭔지 확인해보기..
                    print("***********", img_from_form)
                    print("***********", img_from_form["image"])

                    # image의 fk field(article)를, 위에서 user까지 지정한 article로 설정하고 image field 지정
                    complete_image = ArticleImage(article=complete_ArticleForm, image=image_file)
                    complete_image.save()

            return HttpResponseRedirect(reverse("articleapp:list"))  # 수정하자!! 작성된 게시글 페이지로 이동하도록
            # return HttpResponseRedirect(reverse("articleapp:list", kwargs={"pk": request.POST.}))


        else:
            error_msg = [ArticleForm.errors, formset.errors]
            return render(request, template_name="articleapp/creation_failure.html",
                          context={"error_msg": error_msg})


    else:
        ArticleForm = ArticleCreationForm()
        formset = ImageFormSet(queryset=ArticleImage.objects.none())

        return render(request, template_name="articleapp/createArticle.html",
                      context={"articleForm": ArticleForm, "formset": formset})








