# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Studentapplication, Student, User, Staff
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserForm, StudentregistartionForm, StaffuserForm, StaffregistrationForm
# Create your views here.


def index(request):
    return render(request, 'collegesite/base.html', {})


def student_application(request):
    if request.method == 'POST':

        Studentapplication.objects.create(
            name = request.POST['name'],
            gender = request.POST['gender'],
            email = request.POST['email'],
            dob = request.POST['dob'],
            address = request.POST['address'],
            nationality = request.POST['nationality'],
            department = request.POST['department'],
            sccmemo = request.FILES['sscmemo'],
            intermemo = request.FILES['intermemo'],

                )
        return HttpResponseRedirect(reverse('collegesite:index'))
    else:
        return render(request, 'collegesite/student_application.html', {})


def student_registartion(request):
    if request.method == "GET":
        form1 = UserForm()
        form2 = StudentregistartionForm()
        return render(request, 'collegesite/student_registartion.html', {'form1':form1, 'form2':form2})
    form1 = UserForm(request.POST)
    form2 = StudentregistartionForm(request.POST, request.FILES)
    email = request.POST['email']
    studenta = Studentapplication.objects.filter(email=email, is_verified=True)
    studentb = Studentapplication.objects.get(email=email, is_verified=True)
    if studenta.exists() and form2.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username,email,password)
        profile = form2.save(commit=False)
        profile.user = user
        profile.name = studentb
        profile.save()
        return HttpResponseRedirect(reverse('collegesite:index'))
    return render(request, 'collegesite/student_registartion.html', {'form1':form1, 'form2':form2})


def staff_registration(request):
    if request.method == 'POST':

        form1 = StaffuserForm(request.POST)
        form2 = StaffregistrationForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                email = request.POST['email']
                user = User.objects.create_user(username,email,password)
                profile = form2.save(commit=False)
                profile.user = user
                profile.save()
                return HttpResponseRedirect(reverse('collegesite:index'))
    else:
        form1 = StaffuserForm()
        form2 = StaffregistrationForm()
    return render(request, 'collegesite/staff_registration.html', {'form1':form1,'form2':form2})


@login_required
def student_profile(request):
    stnd = Student.objects.get(user__username=request.user)
    return render(request, 'collegesite/student_profile.html', {'stnd': stnd})


@login_required
def staff_profile(request):
    s = Staff.objects.get(user__username=request.user.username)
    return render(request, 'collegesite/staff_profile.html', {'s': s})


def student_list(request):
    list_of_selected_students = Studentapplication.objects.filter(is_verified=True)
    return render(request, 'collegesite/student_list.html', {'list_of_selected_students':list_of_selected_students})


def user_login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        s = Studentapplication.objects.filter(email=email, is_verified=True)
        user = authenticate(request, username=username, password=password)

        if user is not None and s.exists():


            login(request,user)

            return HttpResponseRedirect(reverse('collegesite:student_profile'))

        elif user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('collegesite:staff_profile'))

        else:
            return render(request, 'collegesite/login.html', {})
    else:
        return render(request, 'collegesite/login.html', {})

"""
def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #s = Studentapplication.objects.get(email__email, is_verified=True)

        user = authenticate(request, username=username, password=password)
        if user is not None:


            login(request,user)

            return HttpResponseRedirect(reverse('collegesite:student_profile'))

        else:
            return render(request, 'collegesite/login.html', {})
    else:
        return render(request, 'collegesite/login.html', {})
"""
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('collegesite:index'))


@login_required
def staff(request):
    staffs = Staff.objects.all()
    return render(request, 'collegesite/staff_all.html', {'staffs' : staffs})
@login_required
def students(request):
    students = Student.objects.all()
    return render(request, 'collegesite/students.html', {'students': students})


@login_required
def staff_department(request):
    #import ipdb; ipdb.set_trace()
    stu_dep = Student.objects.get(user=request.user)
    staff_department = Staff.objects.filter(department__exact=stu_dep.name.department)
    return render(request, 'collegesite/staff_department.html', {'staff_department' : staff_department})

