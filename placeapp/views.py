from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, FormView

from articleapp.forms import ArticleCreationForm, ArticleImageForm
from articleapp.models import ArticleImage
from placeapp.forms import PlaceCreationForm, PlaceSearchForm
from placeapp.models import Place
from sitecategoryapp.models import SiteCategory, ChildCategory


def create_place(request):

    if request.method == "POST":
        place_form = PlaceCreationForm(request.POST)

        # 체크박스 체크한 요소들
        selected_categories = request.POST.getlist("selectedCategories")  # 장소 카테고리 (태그)
        print("selected_categories:", selected_categories)  # ['Bar', 'Cafe']

        if place_form.is_valid():
            complete_place_form = place_form.save(commit=False)

            if not complete_place_form.first_discoverer:
                complete_place_form.first_discoverer = request.user

            print("===========", complete_place_form.first_discoverer)

            place_address_frag = [request.POST.get("mainAddress")]
            if request.POST.get("detailAddress"):
                place_address_frag.append(request.POST.get("detailAddress"))
            if request.POST.get("extraAddress"):
                place_address_frag.append(request.POST.get("extraAddress"))

            place_address = " ".join(place_address_frag)
            complete_place_form.address = place_address

            complete_place_form.save()  # 저장한 후 manytomany 필드(카테고리) 추가 가능

            for category in selected_categories:
                cur = ChildCategory.objects.get(name=category)  # filter 함수는 query를 리턴, get 함수는 object를 리턴
                # print("***********", cur.id)
                complete_place_form.category.add(cur)

            print("*****", complete_place_form.category.all())
            for category in selected_categories:
                cur = ChildCategory.objects.get(name=category)
                print("***", cur.place_set.all())

            return HttpResponseRedirect(reverse("accountapp:helloWorld"))

        else:
            return HttpResponseBadRequest("<h1 style='text-align:center;'>Place creation failed. Please try again.</h1>")

    else:
        place_form = PlaceCreationForm()
        parent_categories = SiteCategory.objects.all()

        return render(request, template_name="placeapp/create.html",
                        context={"form": place_form, "parent_categories": parent_categories})


class PlaceListView(ListView):
    model = Place


class PlaceDetailView(DetailView):
    model = Place
    context_object_name = "current_place"
    template_name = "sitecategoryapp/detail.html"


class ImageFormSet:
    pass


def search_place(request):
    if request.method == "POST":
        searching_place = request.POST.get("searching_place")
        print(searching_place)
        place_list = Place.objects.filter(name__icontains=searching_place)
        print(place_list)
        placeSearchForm = PlaceSearchForm(request.POST)

        articleForm = ArticleCreationForm()
        # 하나의 modelform 을 여러번 쓸 수 있음. 모델, 모델폼, 몇 개의 폼을 띄울건지 갯수
        ImageFormSet = modelformset_factory(ArticleImage, form=ArticleImageForm, extra=5)
        formset = ImageFormSet(queryset=ArticleImage.objects.none())

        return render(request, template_name="articleapp/createArticle.html", context={"searching_place": searching_place,
            "articleForm": articleForm, "formset": formset, "place_list": place_list, "placeSearchForm": placeSearchForm})
    else:
        pass




