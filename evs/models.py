from django.db import models
from django.utils import timezone

class VotingEvent(models.Model):
    event_name = models.CharField(max_length=200, default="")
    pub_date = models.DateTimeField('date created', default=timezone.now)

class Question(models.Model):
    voting_event = models.ForeignKey(VotingEvent, on_delete= models.CASCADE)
    question_text = models.CharField(max_length=1500, default="")
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_text = models.CharField(max_length=200, default="")

