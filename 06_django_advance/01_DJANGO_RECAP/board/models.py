from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse("board:article_detail", kwargs={"article_id": self.id})


class Comment(models.Model):
    content = models.CharField(max_length=200)
    # 300글자 입력시 에러가 아닌 200글자 까지만 저장됨
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # CASCADE 원본이 날라가면 id값도 날라간다(ex, 본문 - 댓글)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)