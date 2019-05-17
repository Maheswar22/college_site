from django import forms
from .models import User,  Student, Staff


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password','email')



class StudentregistartionForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ['user','name']


class StaffuserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password',)



class StaffregistrationForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('name','email', 'age', 'gender', 'department', 'profilepic' )