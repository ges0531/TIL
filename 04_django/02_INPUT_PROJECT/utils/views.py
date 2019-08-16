from django.shortcuts import render, redirect
from art import *
import requests
# Create your views here.


def index(request):
    return render(request, 'utils/index.html')


def art(request):
    fonts = ['3d_diagonal', '5lineoblique', 'alpha', 'larry3d']
    return render(request, 'utils/art.html', {
        'fonts': fonts,
    })


def output(request):
    user_input = request.GET.get('user-input')
    user_font = request.GET.get('user-font')

    if user_input:
        result = text2art(user_input, font=user_font)
        return render(request, 'utils/output.html', {
            'result': result
        })
        # return HttpResponse(user_input)
    else:
        return redirect('/utils/art/')


def throw(request):
    return render(request, 'utils/throw.html')


def catch(request):
    user_menu = request.GET.get('user-menu')
    hungry = ['짜장면', '짬뽕', '볶음밥', '라면', '김밥', '돌솥비빔밥', '양꼬치', '요플레', '치킨', '피자']
    very_hungry = ['탕수육', '팔보채', '닭강정', '라조육', '냉모밀', '오리로스', '치즈김밥']
    if user_menu == 'hungry':
        result = random.sample(hungry, 1)
    else:
        result = random.sample(very_hungry, 1)
    return render(request, 'utils/catch.html', {
        'result': result
    })
