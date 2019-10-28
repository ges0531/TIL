from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:article_id>/article_detail/', views.article_detail, name='article_detail'),
    path('article_create/', views.article_create, name='article_create'),   
    path('<int:article_id>/article_update/', views.article_update, name='article_update'),   
    path('<int:article_id>/article_delete/', views.article_delete, name='article_delete'),   
    path('<int:article_id>/like/', views.like, name='like'),
]