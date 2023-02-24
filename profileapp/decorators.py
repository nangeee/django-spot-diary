from profileapp.models import Profile
from django.http import HttpResponseForbidden


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs["pk"])  # url을 통해 보낸 pk 파라미터 활용
        if profile.user != request.user:  # 만약 pk를 통해 얻은 profile의 user가 실제 request에 담긴 로그인 user와 동일하지 않다면
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)  # 동일하다면 원래 함수 그대로 return

    return decorated
