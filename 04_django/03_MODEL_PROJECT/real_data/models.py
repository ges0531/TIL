from django.db import models

# Create your models here.


class HotIssue(models.Model):
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=10)
    rank = models.IntegerField()
    key = models.CharField(max_length=50)
