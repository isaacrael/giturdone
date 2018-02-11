import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    category = models.CharField(max_length=30)

    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_text = models.CharField(max_length=200)
    answers = models.IntegerField(default=0)
    correct_answer = models.CharField(max_length=200, default='Linus Torvalds')
    total_correct_answers = models.IntegerField(default=0)
    total_wrong_answers = models.IntegerField(default=0)
    image = models.ImageField(upload_to='post_image', blank=True)

    def __unicode__(self):
        return self.answer_text


class Ftq_Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Ftq_Answer(models.Model):
    question = models.ForeignKey(Ftq_Question)
    answer_text = models.CharField(max_length=600)
    knowledge_mastery = models.IntegerField(default=0)
    black_holes_knowledge = models.IntegerField(default=0)
    image = models.ImageField(upload_to='post_image', blank=True)

    def __unicode__(self):
        return self.answer_text

