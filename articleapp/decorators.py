from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from articleapp.models import Article


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs["pk"])  # url을 통해 보낸 pk 파라미터 활용
        if user != request.user:  # 만약 pk를 통해 얻은 user가 실제 request에 담긴 로그인 user와 동일하지 않다면
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)  # 동일하다면 원래 함수 그대로 return

    return decorated


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs["pk"])  # url을 통해 보낸 article의 pk 파라미터 활용
        if article.writer != request.user:  # 만약 pk를 통해 얻은 article writer가 실제 request에 담긴 로그인 user와 동일하지 않다면
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)  # 동일하다면 원래 함수 그대로 return

    return decorated

