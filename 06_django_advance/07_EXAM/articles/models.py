from django.db import models
from django.auth.contrib import get_user_model
# Create your models here.
User = get_user_model()

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    like_users = models.ManyToManyField(User, related_name='like_articles')
