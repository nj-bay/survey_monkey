from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class Answer(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey(User)
#     posted = models.DateTimeField(auto_now=True)
#     url = models.SlugField()
#     quest = models.CharField(max_length=500)

class Question(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    posted = models.DateTimeField(auto_now=True)
    url = models.SlugField()
    quest = models.CharField(max_length=500)

class Survey(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    posted = models.DateTimeField(auto_now=True)
    url = models.SlugField()
    question = models.ForeignKey(Question)

