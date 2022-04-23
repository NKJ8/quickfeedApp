
from django import forms
# from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(forms.Form):

    email = forms.CharField(label='Email address', required=True, error_messages={
        'required': "Email is required",
        'max_length': "Please enter a shorter email"
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    password = forms.CharField(label='Enter password', required=True, error_messages={
        'required': "Password is required",
        'max_length': "Please enter a shorter password"
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    cnf_password = forms.CharField(label='Confirm password', required=True, error_messages={
        'required': "Confirm password is required",
        'max_length': "Please enter a shorter confirm password"
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))


class LoginForm(forms.Form):
    email = forms.CharField(label='Email address', required=True, error_messages={
        'required': "Email is required",
        'max_length': "Please enter a shorter email"
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    password = forms.CharField(label='Enter password', required=True, error_messages={
        'required': "Password is required",
        'max_length': "Please enter a shorter password"
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
