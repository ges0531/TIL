from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.http import require_http_methods
from .models import Article, Comment
from .forms import ArticleModelForm, CommentModelForm, ArticleForm
from IPython import embed



# def new_article_with_form(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             article = Article()
#             article.title = form.cleaned_data.get('title')
#             article.content = form.cleaned_data.get('content')
#             article.save()
#             return redirect(article)


# CRUD
@require_http_methods(['GET', 'POST'])
def new_article(request):
    # 요청이 GET/POST 인지 확인한다.
    # 만약 POST 라면
    if request.method == 'POST':
        # ArticleModelForm 의 인스턴스를 생성하고 Data 를 채운다(binding).
        form = ArticleModelForm(request.POST)
        # binding 된 form 이 유효한지 체크한다.
        if form.is_valid():
            # 유효하다면 form 을 저장한다.
            article = form.save()
            # 저장한 article detail 로 redirect 한다.
            return redirect(article)  # redirect('board:article_detail', article.id)
        # form 이 유효하지 않다면,
        # else:
        #     # 유효하지 않은 입력데이터를 담은 HTML과 에러메세지를 사용자한테 보여준다.
        #     return render(request, 'board/new.html', {
        #         'form': form,
        #     })
    # GET 이라면
    else:
        # 비어있는 form(HTML 생성기)을 만든다.
        form = ArticleModelForm()
    # form 과 html 을 사용자에게 보여준다.
    return render(request, 'board/new.html', {
        'form': form,
    })


@require_GET
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles,
    })


@require_http_methods(['GET', 'POST'])
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleModelForm(instance=article)
    return render(request, 'board/edit.html', {
        'form': form,
    })


@require_GET
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comment_set.all().order_by('-id')  # Comment.objects.filter(article_id=article.id)
    comment_form = CommentModelForm()

    return render(request, 'board/detail.html', {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    })


@require_POST  # Database 의 영향을 주면 POST
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('board:article_list')


def index(request):
    pass


@require_POST
def new_comment(request, article_id):  # board/articles/N/comments/new
    article = get_object_or_404(Article, id=article_id)
    form = CommentModelForm(request.POST)  # 목적이 저장하려고 만듦, 화면이 필요할 때는 ()를 비워둠
    # embed()
    if form.is_valid():
        # comment = Comment() +
        # comment.content = request.POST.get('content') == comment = form.save(commit=False)
        comment = form.save(commit=False)  # comment 변수를 만들 필요가 없음 저장이 중요 화면으로 보여줄게 아님
        comment.article_id = article.id
        comment.save()
    return redirect(article)


@require_POST
def delete_comment(request, article_id, comment_id):
    # article = get_object_or_404(Article, id=article_id)
    # comment = get_object_or_404(Comment, id=comment_id)
    # if comment in article.comment_set.all():  # article과 comment가 연관이 있는지
    #     comment.delete()
    # return redirect(article)

    comment = get_object_or_404(Comment, id=comment_id, article_id=article_id)
    comment.delete()
    return redirect(comment.article)

# comment = Comment()
    # comment.content = request.POST.get('comment_content')
    # comment.article_id = article.id
    # comment.save()


# from .models import Article
# from .forms import ArticleModelForm


# @require_GET
# def index(request):
#     return render(request, 'board/index.html')


# @require_GET
# def list(request):
#     articles = Article.objects.all()  # [<A1>, <A2>, <A3>,...]

#     return render(request, 'board/list.html', {
#         'articles': articles,
#     })


# @require_GET
# def detail(request, id):
#     article = get_object_or_404(Article, id=id)
#     return render(request, 'board/detail.html', {
#         'article': article,
#     })


# def new(request):
#     if request.method == 'POST':
#         form = ArticleModelForm(request.POST)

#         if form.is_valid():
#             article = form.save()
#             return redirect(article)
#     else:
#         form = ArticleModelForm()
#     return render(request, 'board/new.html', {
#         'form': form,
#     })


# def edit(request, id):
#     article = get_object_or_404(Article, id=id)
#     if request.method == 'POST':
#         article.title = request.POST.get('title')
#         article.content = request.POST.get('content')
#         article.save()
#         return redirect(article)
#     else:
#         return render(request, 'board/edit.html', {
#             'article': article,
#         })


# @require_POST
# def delete(request, id):
#     article = get_object_or_404(Article, id=id)
#     article.delete()
#     return redirect('board:list')
