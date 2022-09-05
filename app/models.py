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