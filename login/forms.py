from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Enter a valid email address.')
    username = forms.CharField(max_length=60, help_text='Required. Enter a valid username.')
    password1= forms.CharField( widget=forms.PasswordInput, help_text='Required. Your password must contain at least 8 characters including a number or symbol,small letter and a capital letter.')
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name', 
            'email', 
            'password1', 
            'password2'
            )
        widgets = {
            'email':forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your first name'}),
            'username':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your last name'}),
           
        }
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())