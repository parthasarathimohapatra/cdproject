from django.db import models
import datetime
from django.utils import timezone

class Employee(models.Model):
    eno=models.IntegerField()
    ename = models.CharField(max_length=100)
    ecity = models.CharField(max_length=50)
    start_time=models.DateTimeField(default=timezone.now,blank=False)
    end_time=models.DateTimeField(default=timezone.now,blank=False)
