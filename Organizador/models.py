from django.db import models

# Create your models here.

class Note(models.Model):

    title=models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    color = models.CharField(max_length=10)
    date = models.DateTimeField()

class Meeting(models.Model):

    title=models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    date = models.DateTimeField()
    place = models.CharField(max_length=250)


class Task(models.Model):

    title=models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    deadline = models.DateTimeField()
    done = models.BooleanField()