from enum import unique

from django.db import models as m

# Create your models here.
class student(m.Model):
    name=m.CharField(max_length=30)
    age=m.IntegerField()
    course=m.CharField(max_length=30)
    mark=m.IntegerField()

class course(m.Model):
    MODE_CHOICES = [
        ('hybrid', 'Hybrid'),
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]
    course_name = m.CharField(max_length=30)
    fee = m.IntegerField()
    duration = m.CharField(max_length=30)
    instructor = m.CharField(max_length=30)
    mode = m.CharField(choices=MODE_CHOICES)
