from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.index, name='index'),  # /board/ == board:index
    # Create 글 쓰기(new) render
    path('students/new/', views.new, name='new'),
    # Create 글 저장(create)
    path('students/create/', views.create, name='create'),

    # Read 글 목록(list) render(화면이 필요한 애들)
    path('students/', views.list, name='list'),
    # Read 글 상세(detail) render
    path('students/<int:id>/', views.detail, name='detail'),

    # Update 글 수정쓰기(edit) render
    path('students/<int:id>/edit/', views.edit, name='edit'),
    # Update 글 실제수정(update)
    path('students/<int:id>/update/', views.update, name='update'),

    # Delete 글 삭제(delete)
    path('students/<int:id>/delete/', views.delete, name='delete'),
]
