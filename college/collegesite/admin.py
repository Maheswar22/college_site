# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Staff, Student, Studentapplication

# Register your models here.
admin.site.register(Studentapplication)
admin.site.register(Student)
admin.site.register(Staff)
