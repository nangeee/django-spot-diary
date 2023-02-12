from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from accountapp.views import helloWorld, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

### app_name - 도메인 네임 설정?
# 127.0.0.1:8000/account/helloWorld와 같이 주소 접속 - 번거로움
# accountapp:helloWorld 로 접속할 수 있도록 설정 가능. 여기서 helloWorld는 urlpatterns에서 지정한 name 파라미터.
# 즉 도메인 네임을 설정하는 것이라 할 수 있음
# 추후에 관련 함수를 살펴볼 예정
app_name = "accountapp"


urlpatterns = [
    path("helloWorld/", helloWorld, name="helloWorld"),
    path("createAccount/", AccountCreateView.as_view(), name="createAccount"),
    path("login/", LoginView.as_view(template_name="accountapp/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("detail/<int:pk>", AccountDetailView.as_view(), name="detail"),
    path("update/<int:pk>", AccountUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", AccountDeleteView.as_view(), name="delete"),
]



