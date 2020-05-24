from .models import Emp
from django import forms
from django.contrib.auth.models import User

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']