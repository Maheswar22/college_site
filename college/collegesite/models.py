# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
import os

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

@receiver(post_delete, sender=Studentapplication)
def auto_delete_file(sender, instance, **kwargs):
    """
    Deletes th efile from the filesystem
    """
    if instance.sccmemo and instance.intermemo:
        if os.path.isfile(instance.sccmemo) and os.path.isfile(instance.intermemo):
            os.remove(instance.sscmemo) and os.remove(instance.intermemo)


class Student(TimeStampedModel):

    name = models.OneToOneField(Studentapplication, on_delete=models.CASCADE, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father = models.CharField(max_length=40)
    mother = models.CharField(max_length=40)
    profilepic = models.ImageField()

    def __str__(self):
        return "{} {}".format(self.name.name, self.user.username)
@receiver(post_delete, sender=Student)
def auto_delete_file(sender, instance, **kwargs):
    """
    Deletes the files from the filesystem
    """
    if instance.profilepic:
        if os.path.isfile(instance.profilepic.path):
            os.remove(instance.profilepic.path)

@receiver(pre_save, sender=Student)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes the old file from filesystem after updating new
    """
    if not instance.pk:
        return False
    try:
        old_file = Students.objects.get(pk=instance.pk).profilepic
    except Student.DoesNotExist:
        return False
    new_file = instance.profilepic
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


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

@receiver(post_delete, sender=Staff)
def auto_delete_file(sender, instance, **kwargs):
    """
    Deletes files filesystem
    """
    if instance.profilepic:
        if os.path.isfile(instance.profilepic.path):
            os.remove(instance.profilepic.path)


@receiver(pre_save, sender=Staff)
def auto_delete_file_on_change(sender, instance, **kwagrs):
    """
    Deletes th old file from filesystem
    """
    if not instance.pk:
        return False
    try:
        old_file = Staff.objects.get(pk=instance.pk).profilepic
    except Staff.DoesNotExist:
        return False
    new_file = instance.profilepic
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
