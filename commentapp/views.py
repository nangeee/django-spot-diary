from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = "commentapp/create.html"

    def form_valid(self, form):  # commentapp/forms.py의 CommentCreationForm에서 전송한 데이터가 form 파라미터에 전달됨
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        # commentapp/create.html에서 post 방식으로 전송된 hidden input article_pk를 통해, 댓글이 귀속될 article 설정
        temp_comment.writer = self.request.user  # request를 보낸 request.user를 temp_comment의 user로
        temp_comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("articleapp:detail", kwargs={"pk": self.object.article.pk})


@method_decorator(comment_ownership_required, "get")
@method_decorator(comment_ownership_required, "post")
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    context_object_name = "current_comment"
    template_name = "commentapp/delete.html"
    # template_name = "commentapp/delete.html"  # 이 설정을 안 함으로써 오류 발생


    def get_success_url(self):
        return reverse("articleapp:detail", kwargs={"pk": self.object.article.pk})

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

