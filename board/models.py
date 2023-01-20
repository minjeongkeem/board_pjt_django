from django.db import models
from  django.conf import settings
# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=10)
    Language = models.CharField(max_length=10,)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')


class Comment(models.Model):
    name = models.CharField(max_length=10)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    
