import datetime
from django.utils import timezone
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # make sure it display the question_text instead of Question object
    def __str__(self):
    	# Change name __str__ by __unicode__ on Python 2
    	return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <=now


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # make sure it display the choice_text instead of Question object
    def __str__(self):
    	# Change name __str__ by __unicode__ on Python 2
    	return self.choice_text