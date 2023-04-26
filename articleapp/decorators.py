from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs["pk"])  # url을 통해 보낸 article의 pk 파라미터 활용
        if article.writer != request.user:  # 만약 pk를 통해 얻은 article writer가 실제 request에 담긴 로그인 user와 동일하지 않다면
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)  # 동일하다면 원래 함수 그대로 return

    return decorated

