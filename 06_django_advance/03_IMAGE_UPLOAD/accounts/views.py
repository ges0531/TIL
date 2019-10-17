from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout  # as ~라고 부르겠다

@require_http_methods(['GET', 'POST'])
def signup(request):  # new_user
    if request.user.is_authenticated:  # 사용자가 login 한 상태라면, 무시
        return redirect('sns:posting_list')
    # 사용자가 회원가입할 데이터를 보냈다는 뜻
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('sns:posting_list')
            
    else:  # 사용자가 회원가입 HTML 을 달라는 뜻
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

@require_http_methods(['GET', 'POST'])
def login(request):
    # from IPython import embed; embed()
    if request.user.is_authenticated:  # 사용자가 login 한 상태라면, 무시
        return redirect('sns:posting_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)  # request.POST == data
        if form.is_valid():
            auth_login(request, form.get_user())
            response = redirect('sns:posting_list')
            # response.set_cookie(key='nickname', value='idiot') # max_age=5 가 없으면 영구저장
            return response
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })


def logout(request):
    auth_logout(request)
    return redirect('sns:posting_list')

# Create your views here.
