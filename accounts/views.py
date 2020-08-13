from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView # django에서 만들어둔 로그인뷰 클래스

# Create your views here.

def signup(request):
    regi_form = UserCreationForm() # django에서 만들어져있는 모델폼
    if request.method == 'POST':
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')
    return render(request, 'signup.html', {'regi_form':regi_form})

# 로그인뷰 클래스 오버라이딩
class MyLoginView(LoginView):
    template_name = 'login.html'