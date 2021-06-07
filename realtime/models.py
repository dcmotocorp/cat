from django.db import models
from datetime import datetime

from django.db.models.fields import DateTimeField 
# Create your models here.

class Time(models.Model):
    time=DateTimeField()