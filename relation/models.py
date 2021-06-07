from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.

#many to many 

class Person(models.Model):
    name=models.CharField(max_length=50)

class Group(models.Model):
    group_name=models.CharField(max_length=50)
    member=models.ManyToManyField(Person,through='Membership')

class Membership(models.Model):
    person=models.ForeignKey(Person,on_delete=CASCADE)
    group=models.ForeignKey(Group,on_delete=CASCADE) 
