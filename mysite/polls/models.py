import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_test = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('Date Published')

    def was_pub_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.question_test

class Choice(models.Model):
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text