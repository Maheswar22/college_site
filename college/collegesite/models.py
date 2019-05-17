# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modeified_at = models.DateTimeField(auto_now_add=True)

    class meta:
        abstract = True

class Studentapplication(TimeStampedModel):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )

    DEPARTMENT_CHOICES = (
        ('CE', 'Civil Engineering'),
        ('CSE', 'Computer Science Engineering'),
        ('ECE', 'Electronics Communtication Engineering'),
        ('EEE', 'Electronics Electrical Engineering'),
        ('ME', 'Mechanical Engineering')
    )
    name = models.CharField(max_length=40)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    dob = models.DateField()
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)
    sccmemo = models.FileField()
    intermemo = models.FileField()
    address = models.TextField(max_length=100)
    nationality = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.name, self.is_verified)

    def delete(self):
        self.sccmemo.delete()
        self.intermemo.delete()
        super(Studentapplication, self).delete()


class Student(TimeStampedModel):

    name = models.OneToOneField(Studentapplication, on_delete=models.CASCADE, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father = models.CharField(max_length=40)
    mother = models.CharField(max_length=40)
    profilepic = models.ImageField()

    def __str__(self):
        return "{} {}".format(self.name.name, self.user.username)
    def delete(self, ):
        self.profilepic.delete()
        super(Student, self).delete()
class Staff(TimeStampedModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    DEPARTMENT_CHOICES = (
        ('CE', 'Civil Engineering'),
        ('CSE', 'Computer Science Engineering'),
        ('ECE', 'Electronics Communtication Engineering'),
        ('EEE', 'Electronics Electrical Engineering'),
        ('ME', 'Mechanical Engineering')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)
    profilepic = models.ImageField()

    def __str__(self):
        return "{} {}".format(self.name, self.user.username)
    def delete(self,*args, **kwargs):
        self.profilepic.delete()
        super(Student, self).delete()


