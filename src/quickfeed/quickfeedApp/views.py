from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request handler
# Action

def homepage(request):
        # return HttpResponse('Hello');
       # return render(request,'hello.html',{'name': 'Nitesh'})
        # return render(request,'hello.html',{'name': 'Nitesh'})
        return render(request,'homepage.html',{'name': 'Nitesh'})