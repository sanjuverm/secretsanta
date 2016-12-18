from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) #what would you like for Christmas
    pub_date = models.DateTimeField('date published') #answer response time


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #what would you like for christmas
    choice_text = models.CharField(max_length=200) #dogs, cats, bears
    votes = models.IntegerField(default=0) #up vote/ down vote (up vote by 1 if gift purchased) 
