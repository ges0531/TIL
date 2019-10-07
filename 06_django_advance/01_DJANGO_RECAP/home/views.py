from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'home/index.html')


def guess(request):
    return render(request, 'home/guess.html')


def answer(request):
    
    count = 0
    if request.POST.get('q1') == '김은수':
        count += 1
    if request.POST.get('q2') == '제육볶음':
        count += 1
    if request.POST.get('q3') == 'AB':
        count += 1

    # 채점
    return render(request, 'home/answer.html', {
        'count': count,
    })
