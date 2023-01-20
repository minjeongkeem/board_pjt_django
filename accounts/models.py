from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username
        
    Language_Choices = (
        ('Python','Python'),
        ('C/C++', 'C/C++' ),
        ('Java', 'Java'),
        ('Kotlin', 'Kotlin'),
        ('Swift', 'Swift'),
        ('Javascript', 'Javascript'),)
    language = models.CharField(max_length=10, choices=Language_Choices)