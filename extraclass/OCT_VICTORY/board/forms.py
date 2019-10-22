from django import forms
from .models import Article

# Form / ModelForm : 1. Data Validation 2. HTML 생성

class ArticleForm(forms.ModelForm):
    # 1. HTML 을 어떻게 만들것인가.
    # 2. 검증을 한다면, 어떤 조건으로 검증할 것인가.
    # 3. 만약 아무것도 적지 않는다면.
        # 1. ModelForm 은 Model 을 알고 있기 때문에,
        # 2. 각 Model 을 읽고, 알아서 HTML + 검증을 합니다.
    title = forms.CharField(min_length=2, max_length=200)
    # content 에 대하여 어떤 검증/HTML 관련해서 적지 않았다 => models.Article 의 content 항목을 보고 할일을 한다.
    class Meta:
        model = Article
        # fields 에 적힌 컬럼은 검증 하겠다.
        fields = ('title', 'content', )


class CommentForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)

    class Meta:
        model = Comment
        fields = ('content', )  # []: 요소 갯수에 상관없이 iterable | (): 요소 갯수가 1이면 단일 값. 2 이상이면 Tuple(iterable)