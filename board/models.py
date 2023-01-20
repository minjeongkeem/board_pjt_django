from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField(max_length=100)


class Content(models.Model):
    name = models.CharField(max_length=10)
    use_language = models.CharField(max_length=20)
    

    
