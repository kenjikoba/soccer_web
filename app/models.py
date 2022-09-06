from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class data(models.Model):
    full_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    height_diff = models.IntegerField(default=0)
    weight_diff = models.IntegerField(default=0)
    attributes = models.CharField(max_length=200)
    youtube1_title = models.CharField(max_length=200)
    youtube1_image = models.CharField(max_length=200)
    youtube1_url = models.CharField(max_length=200)
    youtube2_title = models.CharField(max_length=200)
    youtube2_image = models.CharField(max_length=200)
    youtube2_url =  models.CharField(max_length=200)
    youtube3_title =  models.CharField(max_length=200)
    youtube3_image = models.CharField(max_length=200)
    youtube3_url = models.CharField(max_length=200)

class user_data(models.Model):
    age = models.CharField(max_length=200)
    male_height = models.IntegerField(default=0)
    male_weight = models.IntegerField(default=0)
    female_height = models.IntegerField(default=0)
    female_weight = models.IntegerField(default=0) 

import uuid
from django.utils import timezone
 
class UserInput(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # date = models.DateField(verbose_name='日付', default=timezone.now)
    # title = models.CharField(verbose_name='タイトル', max_length=40)
    # text = models.CharField(verbose_name='本文', max_length=200)
    # created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
    # updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    height = models.IntegerField(verbose_name='身長', default=0)
    weight = models.IntegerField(verbose_name='体重', default=0)
    age = models.CharField(verbose_name='年齢', max_length=200, blank=True)
    position = models.CharField(verbose_name='ポジション', max_length=200, blank=True)
    attributes = models.CharField(verbose_name='特徴', max_length=200, blank=True)