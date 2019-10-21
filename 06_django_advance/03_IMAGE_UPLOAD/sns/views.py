from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Posting, Comment
from .forms import PostingModelForm, CommentModelForm


# login 이 x 면 => 무조건 /account/login/
@require_GET
def posting_list(request):
    # nickname = request.COOKIES.get('nickname')
    postings = Posting.objects.all()
    return render(request, 'sns/posting_list.html', {
        'postings': postings,
        # 'nickname': nickname,
    })

@login_required
@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comments.all()  # posting.comment_set 이 아닌 이유는 Model => related_name
    return render(request, 'sns/posting_detail.html', {
        'posting': posting,
        'comments': comments,
    })


# @require_POST
# def create_posting(request):
#     posting = Posting()
#     posting.content = request.POST.get('content')
#     posting.icon = ''
#     posting.image = request.FILES.get('image')
#     posting.save()
#     return redirect(posting)  # redirect('sns:posting_detail', posting.id)

@login_required
@require_POST
def create_posting(request):
    form = PostingModelForm(request.POST, request.FILES)  # 검증 & 저장 준비
    if form.is_valid():  # 검증!
        posting = form.save(commit=False)  # 저장 => Posting 객체 return
        posting.user = request.user
        posting.save()
        return redirect(posting)  # 성공하면 detail page
    else:
        return redirect('sns:posting_list')  # 실패하면 list page

@login_required
@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.user == posting.user:
        posting.delete()
    return redirect('sns:posting_list')

@login_required
@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentModelForm(request.POST)  # content 만 값을 확인
    if form.is_valid():  # content 만 값을 검증
        comment = form.save(commit=False)  # 아직 posting_id 가 비어있기 때문에, 저장하는 척 만 하고 Comment 객체 return
        comment.posting = posting
        comment.user = request.user
        comment.save()
    return redirect(posting)

@login_required
@require_POST
def delete_comment(request, comment_id, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = get_object_or_404(Comment, id=comment_id, posting_id=posting_id)
    comment.delete()
    return redirect(posting)


@login_required
@require_POST
def toggle_like(request, posting_id):
    user = request.user
    posting = get_object_or_404(Posting, id=posting_id)
    if posting.like_users.filter(id=user.id).exists():
        posting.like_users.remove(user)
        is_like = False
    else:
        posting.like_users.add(user)  # Create
        is_like = True
    return redirect(posting)