from django import forms
from django.core.validators import validate_email
# from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(forms.Form):

    email = forms.EmailField(label='Email address', required=True,validators=[validate_email], error_messages={
        'required': "Email is required",
        'max_length': "Please enter a shorter email"
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    username = forms.CharField(label='Username', required=True, error_messages={
        'required': "Username is required",
       
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    password = forms.CharField(label='Enter password', required=True, error_messages={
        'required': "Password is required",
        'max_length': "Please enter a shorter password"
    }, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    cnf_password = forms.CharField(label='Confirm password', required=True, error_messages={
        'required': "Confirm password is required",
        'max_length': "Please enter a shorter confirm password"
    }, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    name = forms.CharField(label='Full Name', required=True, error_messages={
        'required': "Full Name is required",
       
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    
    dob = forms.DateField(label='Date of Birth', required=True, error_messages={
        'required': "Date of Birth is required",
       
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    address = forms.CharField(label='Address', required=True, error_messages={
        'required': "Address is required",
        
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    phone = forms.CharField(label='Phone Number', required=True, error_messages={
        'required': "Phone Number is required",
        
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

    is_service_provider = forms.BooleanField(label="Login as service provider",required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input me-2 ml-2'}))

class SignUpFormBusiness(forms.Form):

    email = forms.EmailField(label='Email address', required=True,validators=[validate_email], error_messages={
        'required': "Email is required",
        'max_length': "Please enter a shorter email"
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    username = forms.CharField(label='Username', required=True, error_messages={
        'required': "Username is required",
       
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    password = forms.CharField(label='Enter password', required=True, error_messages={
        'required': "Password is required",
        'max_length': "Please enter a shorter password"
    }, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    cnf_password = forms.CharField(label='Confirm password', required=True, error_messages={
        'required': "Confirm password is required",
        'max_length': "Please enter a shorter confirm password"
    }, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    name = forms.CharField(label='Full Name', required=True, error_messages={
        'required': "Full Name is required",
       
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    address = forms.CharField(label='Address', required=True, error_messages={
        'required': "Address is required",
        
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    phone = forms.CharField(label='Phone Number', required=True, error_messages={
        'required': "Phone Number is required",
        
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    
    city = forms.CharField(label='City', required=True, error_messages={
        'required': "City is required",
       
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    state = forms.CharField(label='State', required=True, error_messages={
        'required': "State is required",
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    zipcode = forms.CharField(label='Zip code', required=True, error_messages={
        'required': "Zip code is required",
    }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    # is_open = forms.BooleanField(label='Is Open', required=True, error_messages={
    #     'required': "Is Open is required",
    # }, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    # descriptions = forms.CharField(label='Descriptions', required=True, error_messages={
    #     'required': "Descriptions is required",
    # }, widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
