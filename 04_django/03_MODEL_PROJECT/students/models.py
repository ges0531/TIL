from django.db import models

# Create your models here.


class Student(models.Model):
    # Modeling
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    github_id = models.CharField(max_length=50)


class Menu(models.Model):
    name = models.CharField(max_length=10)
    price = models.FloatField()
    category = models.CharField(max_length=50)

    # name : 메뉴이름 STRING
    # price: 가격 FLOAT
    # category: 카테고리 STRING
