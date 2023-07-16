from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.utils.text import slugify
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import *
from articleapp.models import *
from commentapp.forms import CommentCreationForm


@login_required
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

            return HttpResponseRedirect(reverse("articleapp:detail", kwargs={"pk": complete_ArticleForm.pk}))
            # return HttpResponseRedirect(reverse("articleapp:list"))  # 수정하자!! 작성된 게시글 페이지로 이동하도록
            # return HttpResponseRedirect(reverse("articleapp:list", kwargs={"pk": request.POST.}))


        else:
            error_msg = [ArticleForm.errors, formset.errors]
            return render(request, template_name="articleapp/creation_failure.html",
                          context={"error_msg": error_msg})

    else:
        articleForm = ArticleCreationForm()
        formset = ImageFormSet(queryset=ArticleImage.objects.none())

        return render(request, template_name="articleapp/createArticle.html",
                      context={"articleForm": articleForm, "formset": formset})


# DetailView에는 get 메서드만 존재하므로 get 메서드에만 데코레이터 적용.
# 또는 leftmost 파라미터로 LoginRequiredMixin 전달
@method_decorator(login_required, "get")
class ArticleDetailView(DetailView, FormMixin):
    model = Article
    context_object_name = "current_article"
    template_name = "articleapp/detail.html"
    form_class = CommentCreationForm


# @method_decorator(article_ownership_required, "get")
# @method_decorator(article_ownership_required, "post")
# class ArticleUpdateView(UpdateView):
#     model = Article
#     context_object_name = "current_article"
#     form_class = ArticleCreationForm
#     template_name = "articleapp/update.html"
#
#     def get_success_url(self):
#         # self.object는 article
#         # 해당 article의 pk
#         return reverse("articleapp:detail", kwargs={"pk": self.object.pk})


@article_ownership_required
def ArticleUpdateView(request, pk):
    # 하나의 modelform 을 여러번 쓸 수 있음. 모델, 모델폼, 몇 개의 폼을 띄울건지 갯수
    ImageFormSet = modelformset_factory(ArticleImage, form=ArticleImageForm, extra=5, can_delete=False)

    # fetch the object related to passed id
    article_obj = get_object_or_404(Article, pk=pk)
    img_obj_list = ArticleImage.objects.select_related().filter(article=pk)

    # pass the object as instance in form
    # form = ArticleCreationForm(request.POST or None, instance=article_obj)
    # formset = ImageFormSet(request.POST or None, request.FILES,
    #                        initial=[{"image": i.image} for i in img_obj_list], queryset=ArticleImage.objects.none())
    # for f in formset:
    #     print(f.as_table())

    if request.method == "POST":
        Article.objects.filter(pk=pk).update(
            title=request.POST["title"],
            place_name=request.POST["place_name"],
            address=request.POST["address"],
            content=request.POST["content"]
        )

        ### post에서의 formset
        formset = ImageFormSet(request.POST, request.FILES, queryset=ArticleImage.objects.none())

        # save the data from the form and
        # redirect to detail_view
        if formset.is_valid():

            for img_from_form in formset.cleaned_data:
                print("valid22", img_from_form)
                # ArticleImageForm에 입력된 이미지 하나하나 저장 *** 원래 이미지는 어떻게 삭제 ?? ㅠㅠㅠㅠㅠ
                if img_from_form:
                    print("valid33", img_from_form["image"])
                    image_file = img_from_form["image"]

                    # image의 fk field(article)를, 현재 article로 설정하고 image field 지정
                    complete_image = ArticleImage(article=article_obj, image=image_file)
                    complete_image.save() # 각각의 image와 현재 article을 연결한 후 저장

            return HttpResponseRedirect(reverse("articleapp:detail", kwargs={"pk": pk}))
            # return HttpResponseRedirect("/" + id)

    else:  # GET method
        form = ArticleCreationForm(request.POST or None, instance=article_obj)
        ### get에서의 formset
        formset = ImageFormSet(request.POST or None,
                               initial=[{"image": i.image} for i in img_obj_list], queryset=ArticleImage.objects.none())

        return render(request, template_name="articleapp/update.html",
                  context={"form": form, "formset": formset, "current_article": article_obj})



@method_decorator(article_ownership_required, "get")
@method_decorator(article_ownership_required, "post")
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = "current_article"
    success_url = reverse_lazy("articleapp:list")
    template_name = "articleapp/delete.html"


@method_decorator(login_required, "get")
class ArticleListView(ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "articleapp/list.html"
    paginate_by = 5  # 한 페이지에 노출되는 객체의 수 (article 수)




