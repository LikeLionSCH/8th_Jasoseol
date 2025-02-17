from django.shortcuts import render, redirect, get_object_or_404
from .forms import JssForm, CommentForm
from .models import Jasoseol, Comment
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# from django.http import Http404

# Create your views here.

def index(request):
    all_jss = Jasoseol.objects.all()
    paginator = Paginator(all_jss, 5)
    page = request.GET.get('page')
    jss_page = paginator.get_page(page)
    return render(request, 'index.html', {'all_jss' : jss_page})

def my_index(request):
    my_jss = Jasoseol.objects.filter(author=request.user) # author가 로그인된 사용자와 같은 자소서들만 filtering
    return render(request, 'index.html', {'all_jss' : my_jss})

@login_required(login_url='/login/') # django의 decorators
def create(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')
    if request.method == 'POST':
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():
            temp_form = filled_form.save(commit=False)
            # commit=False : object 저장을 지연시키고 추가적인 동작이 가능
            temp_form.author = request.user
            temp_form.save()
            return redirect('index')
    jss_form = JssForm()
    return render(request, 'create.html', {'jss_form' : jss_form})

@login_required(login_url='/login/')
def detail(request, jss_id):
    # try:
    #     my_jss = Jasoseol.objects.get(pk=jss_id)
    # except:
    #     raise Http404
    my_jss = get_object_or_404(Jasoseol, pk=jss_id)
    comment_form = CommentForm() # 댓글 모델폼
    return render(request, 'detail.html', {'my_jss':my_jss, 'comment_form':comment_form})

def delete(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    if request.user == my_jss.author:
        my_jss.delete()
        return redirect('index')
    
    raise PermissionDenied # 권한없음 오류

def update(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    if request.user == my_jss.author:
        jss_form = JssForm(instance=my_jss)
        if request.method == 'POST':
            updated_form =  JssForm(request.POST, instance=my_jss)
            if updated_form.is_valid():
                updated_form.save()
                return redirect('index')
        return render(request, 'create.html', {'jss_form':jss_form})

    raise PermissionDenied

def create_comment(request, jss_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        temp_form = comment_form.save(commit=False)
        temp_form.author = request.user
        temp_form.jasoseol = Jasoseol.objects.get(pk=jss_id)
        temp_form.save()
        return redirect('detail', jss_id)

def delete_comment(request, jss_id, comment_id):
    my_comment = Comment.objects.get(pk=comment_id)
    if request.user == my_comment.author:
        my_comment.delete()
        return redirect('detail', jss_id)

    else:
        raise PermissionDenied