from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ArticleModelForm
from .models import Article



def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {
        'articles': articles,
    })


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/article_detail.html', {
        'article': article,
    })


def article_create(request):
    if request.method == "POST":
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:article_detail', article.id)
    else:
        form = ArticleModelForm()
    return render(request, 'articles/form.html', {
        'form': form,
    })

def article_update(requset, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.user != request.user:
        return redirect('articles:article_list')
    if request.method == "POST":
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:article_detail', article.id)
    else:
        form = ArticleModelForm(instance=article)
    return render(request, 'articles/form.html', {
        'form': form,
    })

def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.user != article.user:
        pass
    else:
        article.delete()
    return redirect('articles:article_list')


def like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    if user in article.like_users.all():
        article.like_users.remove(user)
    else:
        article.like_users.add(uesr)
    return redirect('articles:article_list')