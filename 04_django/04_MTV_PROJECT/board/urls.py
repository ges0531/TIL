from django.urls import path
from . import views

urlpatterns = [
    # Create
    path('articles/new/', views.new),  # /board/articles/new/
    path('articles/create/', views.create),  # board/articles/creat
    # Read
    path('articles/', views.index),  # /board/articles/
    path('articles/<int:article_id>/', views.show),  # /board/articles/2
    # Update
    # Delete
    path('articles/<int:article_id>/delete/', views.delete)  # /board/articles/delete

]
