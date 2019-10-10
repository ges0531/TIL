from django import forms
from .models import Article

# forms.Form => Data 입력 및 검증
# forms.ModelForm => Data 입력/검증 + HTML 생성


class ArticleModelForm(forms.ModelForm):
    # 1. Data 입력 및 검증
    # 2. HTML 생성
    title = forms.CharField(min_length=2, max_length=100)
    # content = forms.Textarea

    class Meta:
        model = Article
        fields = '__all__'
