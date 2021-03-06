from django.db import models
from django.urls import reverse
from django.conf import settings # MASTER_APP/settings.py
from faker import Faker


"""
완전히 다 지우고 싶을 때 Table
$ python manage.py migrate <APP_NAME> zero
$ rm <APP_NAME>/migrations/0*

"""
f = Faker()
class Posting(models.Model):  # 주석처리 하고 migrate하면 Table 날라감
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_postings', blank=True)
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')  # CharField일때 default값은 '' IntegerField일 때 0
    image = models.ImageField(blank=True)  # 이미지가 비어있을 수 있다, $ pip install pillow
    created_at = models.DateTimeField(auto_now_add=True)  # 추가 됐을 때만 
    updated_at = models.DateTimeField(auto_now = True)  # 수정이 일어날 때마다
    
    class Meta: 
        ordering = ['-created_at', ]  # created_at 을 descending 내림차순으로.

    # Detail 페이지를 쓸 거라면 만들어요
    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})


    def __str__(self):
        return f'{self.pk}: {self.content[:20]}'


    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            cls.objects.create(
                user_id=1,
                content=f.sentence(),
                icon='fas fa-angrycreative',
            )


class Comment(models.Model):
    # related_name 이 없으면, posting.comment_set / 아래와 같다면, posting.comments
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['-created_at', ]  # created_at 을 descending 내림차순으로.
    

    def __str__(self):
        return f'{self.id}: {self.content[:10]}'


    @classmethod
    def dummy(cls, n, posting_id):
        for _ in range(n):
            cls.objects.create(
                user_id=1,
                posting_id=posting_id,
                content=f.sentence(),
            )