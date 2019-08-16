from django.contrib import admin
from .models import Article
# Register your models here.

# python manage.py createsuperuser

admin.site.register(Article)
