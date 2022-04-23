from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from .forms import SignUpForm
from django.http import HttpResponse


# Create your views here.
# request handler
# Action

def homepage(request):
        return render(request, 'index.html', {'title': 'Welcome to quickfeed'})

def login(request):
       return render(request, 'login.html', {'title': 'Login - Quickfeed'})

def register(request):
       return render(request, 'register.html', {'title': 'Register - Quickfeed'})

def homepageold(request):
        return render(request, 'homepage.html', {'title': 'OLD Welcome to quickfeed'})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.dob = form.cleaned_data.get('dob')
            user.name = form.cleaned_data.get('name')
            user.address = form.cleaned_data.get('address')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            auth_login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})