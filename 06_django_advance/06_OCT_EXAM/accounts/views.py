from django.shortcuts import render, redirect, get_object_or_404
# accounts 에서 import 할 모든 함수들은 django.contrib.auth
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# User 모델을 가져오는 함수
from django.contrib.auth import get_user_model
# accounts 에서 import 할 Model(User), Form(UCF, AF))
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# decorator
from django.contrib.auth.decorators import login_required


# 중요!
def signup(request):
    if request.user.is_authenticated:  # is_authenticated 는 함수가 아님.
        return redirect('articles:article_list')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login 을 하도록 합시다! 인자가 2개다
            auth_login(request, user)
            return redirect('articles:article_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/form.html', {
        'form': form,
    })

# signup 복사해와서 form 바꿔끼기 랑 User바꾸기!
def login(request):
    if request.user.is_authenticated:  # is_authenticated 는 함수가 아님.
        return redirect('articles:article_list')

    if request.method == "POST":
        # AuthForm 은 인자가 2개(request, request.POST)개.
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 성공 => 성공한 user 를 꺼낸다.
            user = form.get_user()
            # login 을 하도록 합시다! 인자가 2개다
            auth_login(request, user)
            # 나는 못해요..
            # return redirect('articles:article_list')
            # 나는 할 수 있어요
            return redirect(request.GET.get('next') or 'articles:article_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/form.html', {
        'form': form,
    })


def logout(request):
    # auth_logout 은 인자 1개
    auth_logout(request)
    return redirect('articles:article_list')
