from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    dob = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    address = forms.CharField(help_text='Enter address')
    name = forms.TextInput(help_text='Enter name')
    phone = forms.TextInput(help_text='Enter phone')

    class Meta:
        model = User
        fields = ('username', 'email','name','phone','dob','address', 'password1', 'password2')
