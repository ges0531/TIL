from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def index(request):
    return render(request, 'classroom/index.html')


def new(request):
    return render(request, 'classroom/new.html')


def create(request):
    student = Student()
    student.name = request.POST.get('name')
    student.age = request.POST.get('age')
    student.major = request.POST.get('major')
    student.save()

    return redirect('classroom:detail', student.id)


def list(request):
    students = Student.objects.all()
    return render(request, 'classroom/list.html', {
        'students': students,
    })


def detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'classroom/detail.html', {
        'student': student,
    })


def edit(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'classroom/edit.html', {
        'student': student,
    })


def update(request, id):
    student = get_object_or_404(Student, id=id)
    student.name = request.POST.get('name')
    student.age = request.POST.get('age')
    student.major = request.POST.get('major')
    student.save()

    return redirect('classroom:detail', student.id)


def delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('classroom:list')
