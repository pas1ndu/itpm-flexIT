from django.forms import ModelForm
from .models import *
from dataclasses import fields

from django.forms import ModelForm
from django import forms

class vacancyform(ModelForm):
        class Meta:
            model = vacancy
            fields = '__all__'

# dileeshana
class CvDetailsForm(ModelForm):
    class Meta:
        model = Cvdetails
        fields = '__all__'
    
# sathma
class ComRegisterForm(ModelForm):
	class Meta:
		model = comregister
		fields ='__all__' 


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','password1','password2']


# pasindu
class StuUserForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
