from django import forms
from .models import User,  Student, Staff, Studentapplication

class DateInput(forms.DateInput):
    input_type = 'date'

class StudentApplicationForm(forms.ModelForm):


    class Meta:
        model = Studentapplication
        exclude = ['is_verified']
        widgets = {
            'dob' : DateInput()
         }

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password','email')
        widgets = {
        'password' : forms.PasswordInput(),
        }


class StudentregistartionForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ['user','name']



class StaffuserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password',)
        widgets = {
        'password' : forms.PasswordInput(),
        }



class StaffregistrationForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('name','email', 'age', 'gender', 'department', 'profilepic' )

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
        'password': forms.PasswordInput(),
        }
