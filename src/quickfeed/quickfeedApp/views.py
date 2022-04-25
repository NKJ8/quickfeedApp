from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from .forms import LoginForm, SignUpForm, SignUpFormBusiness
from django.http import HttpResponse, HttpResponseRedirect
import re
from .models import User, Business

# Create your views here.
# request handler
# Action


def homepage(request):
    return render(request, "index.html", {"title": "Welcome to quickfeed"})


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if(form.is_valid()):
            data = {}

            if(form.cleaned_data['is_service_provider']):
                data['business'] = Business.objects.filter(email = form.cleaned_data['email'], password= form.cleaned_data['password']).values().first()
            else:
                data['user'] = User.objects.filter(email = form.cleaned_data['email'], password= form.cleaned_data['password']).values().first()

            if(data['user']):
                # get user data and send on profile page
                return render(request, 'user-profile.html', {
                    "data": data['user']
                })
            if(data['business']):
                # get user data and send on profile page
                return render(request, 'business-profile.html', {
                    "data": data['business']
                })
            else:
                form.add_error('email', "Please check your details.")
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form": form})


def signup(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if(form.is_valid() and (form.cleaned_data['password'] == form.cleaned_data['cnf_password'])):
            if(form.is_valid() and not(User.objects.filter(username = form.cleaned_data['username']).exists())):
                if(form.is_valid() and ((len(form.cleaned_data['password']) > 12) or re.search(" [^a-zA-Z0-9]",form.cleaned_data['password']) or re.search(" [a-zA-Z]",form.cleaned_data['password']) or re.search(" [0-9]",form.cleaned_data['password']))):
                    user = User(
                        username = form.cleaned_data['username'],
                        email = form.cleaned_data['email'],
                        phone = form.cleaned_data['phone'],
                        address = form.cleaned_data['address'],
                        dob = form.cleaned_data['dob'],
                        password = form.cleaned_data['password'],
                        name = form.cleaned_data['name']
                    )
                    user.save()
                    return render(request, 'thank-you.html', {"title": "Thank you for Registering"})
                else:
                    form.add_error('password', "Password lenght should be atleast 12, should contain A-Z Capital letter, a number 0-9 and a special character")       
            else:
                form.add_error('username', "The username you have entered has been taken.")    
        else:
            form.add_error('cnf_password', "Please confirm password correctly.")
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {
        "form": form,
        "title": "User Signup - Quickfeed"
    })

def signupbusiness(request):
    if request.method == 'POST':
        form = SignUpFormBusiness(request.POST)

        if(form.is_valid() and (form.cleaned_data['password'] == form.cleaned_data['cnf_password'])):
            if(form.is_valid() and not(Business.objects.filter(username = form.cleaned_data['username']).exists())):
                if(form.is_valid() and ((len(form.cleaned_data['password']) > 12) or re.search(" [^a-zA-Z0-9]",form.cleaned_data['password']) or re.search(" [a-zA-Z]",form.cleaned_data['password']) or re.search(" [0-9]",form.cleaned_data['password']))):
                    user = Business(
                        username = form.cleaned_data['username'],
                        email = form.cleaned_data['email'],
                        phone = form.cleaned_data['phone'],
                        address = form.cleaned_data['address'],
                        city = form.cleaned_data['city'],
                        descriptions = form.cleaned_data['descriptions'],
                        password = form.cleaned_data['password'],
                        name = form.cleaned_data['name']
                    )
                    user.save()
                    return render(request, 'thank-you.html', {"title": "Thank you for Registering"})
                else:
                    form.add_error('password', "Password lenght should be atleast 12, should contain A-Z Capital letter, a number 0-9 and a special character")    
            else:
                form.add_error('username', "The username you have entered has been taken.")    
        else:
            form.add_error('cnf_password', "Please confirm password correctly.")
    else:
        form = SignUpFormBusiness()

    return render(request, 'signup-business.html', {
        "form": form,
        "title": "Business User Signup - Quickfeed"
    })

# return HttpResponseRedirect("/thank-you")
# def signup(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  # load the profile instance created by the signal
#             user.dob = form.cleaned_data.get("dob")
#             user.name = form.cleaned_data.get("name")
#             user.address = form.cleaned_data.get("address")
#             user.save()
#             raw_password = form.cleaned_data.get("password1")
#             user = authenticate(username=user.username, password=raw_password)
#             auth_login(request, user)
#             return redirect("homepage")
#     else:
#         form = SignUpForm()
#     return render(request, "signup.html", {"form": form})

def homepageold(request):
    return render(request, "homepage.html", {"title": "OLD Welcome to quickfeed"})



