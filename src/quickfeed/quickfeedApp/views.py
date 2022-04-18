from django.shortcuts import render
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