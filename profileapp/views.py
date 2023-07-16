from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    context_object_name = "current_profile"
    form_class = ProfileCreationForm
    template_name = "profileapp/createProfile.html"

    def form_valid(self, form):  # profileapp/forms.py의 ProfileCreationForm에서 전송한 데이터가 form 파라미터에 전달됨
        temp_profile = form.save(commit=False)  # 실제 DB에 저장하지는 않고 일단 임시로
        temp_profile.user = self.request.user  # request를 보낸 request.user를 temp_profile의 user로
        temp_profile.save()

        return super().form_valid(form)  # 이 line만 작성하면, 원래의 form_valid 함수와 동일

    def get_success_url(self):
        if self.request.POST["next"]:
            return self.request.POST["next"]
            # return HttpResponseRedirect(self.request.POST["next"])
        # self.object는 profile
        # 해당 profile의 user.pk
        return reverse("accountapp:detail", kwargs={"pk": self.object.user.pk})


@method_decorator(profile_ownership_required, "get")
@method_decorator(profile_ownership_required, "post")
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = "current_profile"
    form_class = ProfileCreationForm
    template_name = "profileapp/update.html"

    def get_success_url(self):
        # self.object는 profile
        # 해당 profile의 user.pk
        return reverse("accountapp:detail", kwargs={"pk": self.object.user.pk})



