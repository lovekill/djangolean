#coding=utf-8
from django.db import models
class Question(models.Model):
    question_text = models.CharField(max_length=200,name="gameName")
    pub_data = models.DateTimeField("time")
    models.Model.name="xxxx"
    def __str__(self):
        return self.gameName

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
