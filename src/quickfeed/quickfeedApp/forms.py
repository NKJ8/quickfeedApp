
from django import forms
# from django.contrib.auth.forms import UserCreationForm
from .models import User

<<<<<<< HEAD
class SignUpForm(UserCreationForm):
    dob = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    address = forms.CharField(help_text='Enter address')
    name = forms.TextInput(help_text='Enter name')
    phone = forms.TextInput(help_text='Enter phone')
=======
class SignUpForm(forms.Form):
>>>>>>> b9f63482cd25e1680f9554b82036fb71668db625

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
