from django.urls import path
from .views import signup, MyLoginView
from django.contrib.auth.views import LogoutView # django에서 만들어둔 로그아웃뷰 클래스

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]