from django.db import models
from django.urls import reverse


"""
완전히 다 지우고 싶을 때 Table
$ python manage.py migrate <APP_NAME> zero
$ rm <APP_NAME>/migrations/0*

"""

class Posting(models.Model):  # 주석처리 하고 migrate하면 Table 날라감
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')  # CharField일때 default값은 '' IntegerField일 때 0
    image = models.ImageField(blank=True)  # 이미지가 비어있을 수 있다, $ pip install pillow
    created_at = models.DateTimeField(auto_now_add=True)  # 추가 됐을 때만 
    updated_at = models.DateTimeField(auto_now = True)  # 수정이 일어날 때마다 

    # Detail 페이지를 쓸 거라면 만들어요
    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})


    def __str__(self):
        return f'{self.pk}: {self.content[:20]}'
    