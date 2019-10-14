from django import forms
from .models import Article, Comment

# forms.Form => Data 입력 및 검증 + HTML 제공 => Model 정보모름
# forms.ModelForm => Data 입력/검증 + HTML 제공 => Model 정보를 알고있음


class ArticleForm(forms.Form):
    title = forms.CharField(min_length=2, max_length=100)
    content = forms.CharField()



class ArticleModelForm(forms.ModelForm):
    # 1. Data 입력 및 검증
    # 2. HTML 생성
    title = forms.CharField(min_length=2, max_length=100)
    # content = forms.Textarea

    class Meta:
        model = Article
        fields = '__all__'


class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)  # 200 을 검증

    class Meta:
        model = Comment
        fields = ('content',)  # CommentModelForm 을 검증할 때 content만 검증하겠다(article_id는 검증 x)
