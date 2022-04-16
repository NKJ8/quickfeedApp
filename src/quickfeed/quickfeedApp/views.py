from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request handler
# Action

def homepage(request):
        return render(request, 'index.html', {'title': 'Welcome to quickfeed'})