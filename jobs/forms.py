from django import forms
from django.db.models.base import Model
from django.db.models.fields import DateField
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput
from django import forms

from .models import Client, Employee, Project, Tracker

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('platform','type','handled','status')

class CreateProject(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateTrackerForm(ModelForm):
    class Meta:
        model = Tracker
        fields = '__all__'

class CreateClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class EmployeeAccountForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name','location','profile_pic']

class CreateEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude=['user','profile_pic']
        doj = forms.DateField(
            input_formats=['%m/%d/%Y'],
            widget=forms.DateInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            }), required=False
        )
        dor = forms.DateField(
            input_formats=['%m/%d/%Y'],
            widget=forms.DateInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker2'
            }), required=False
        )        