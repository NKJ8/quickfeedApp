from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from .forms import ForgotPwdForm, LoginForm, SignUpForm, SignUpFormBusiness
from django.http import HttpResponse, HttpResponseRedirect
import re
from .models import User, Business

from pprint import pprint


# Create your views here.
# request handler
# Action


def homepage(request):
    return render(request, "index.html", {"title": "Welcome to quickfeed"})

def about_us(request):
    return render(request, "about-us.html", {"title": "About Us - Quickfeed"})


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if(form.is_valid()):
            data = {}

            if(form.cleaned_data['is_service_provider'] == True):
                data['business'] = Business.objects.filter(username = form.cleaned_data['username'], password= form.cleaned_data['password']).values().first()
            else:
                data['user'] = User.objects.filter(username = form.cleaned_data['username'], password= form.cleaned_data['password']).values().first()

            pprint({"Form": form.cleaned_data, "data": data})
            if('user' in data.keys() and data['user'] != None):
                # get user data and send on profile page
                data = set_session(request, form.cleaned_data['username'], form.cleaned_data['password'])
                
                return render(request, 'user-profile.html', {
                    "data": data
                })
            if( 'business' in data.keys() and data['business'] != None):
                # get user data and send on profile page
                data = set_session(request, form.cleaned_data['username'], form.cleaned_data['password'], False)

                # request.session['email'] = email
                return render(request, 'business-profile.html', {
                    "data": data
                })

            else:
                form.add_error('username', "Please check your login details.")
    else:
        form = LoginForm()

    message = ""
    
    return render(request, "login.html", {"form": form, "message": message})


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

                    data = set_session(request, form.cleaned_data['email'], form.cleaned_data['password'])

                    return render(request, 'user-profile.html', {
                        "data": data
                    })
                else:
                    form.add_error('password', "Password length should be atleast 12, contain atleast one A-Z Capital letter, one number 0-9 and a special character")       
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
                    business = Business(
                        username = form.cleaned_data['username'],
                        email = form.cleaned_data['email'],
                        phone = form.cleaned_data['phone'],
                        address = form.cleaned_data['address'],
                        city = form.cleaned_data['city'],
                        state = form.cleaned_data['state'],
                        zipcode = form.cleaned_data['zipcode'],
                        password = form.cleaned_data['password'],
                        name = form.cleaned_data['name']
                    )
                    business.save()

                    data = set_session(request, form.cleaned_data['email'], form.cleaned_data['password'], False)
                    # pprint({data: data})
                    return render(request, 'business-profile.html', {
                        "data": data
                    })
                    # return redirect('login-page')
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



def homepageold(request):
    return render(request, "homepage.html", {"title": "OLD Welcome to quickfeed"})

def logout(request):
    request.session['is_logged_in'] = False
    request.session['user'] = None
    return redirect("login-page")

def profile(request):
    data = request.session['user']
    return render(request, 'user-profile.html', {
        "data": data
    })


def set_session(request, username, password, user=True):
    request.session['is_logged_in'] = True
    data = {}
    request.session['is_logged_in'] = True
    if(user == True):
        data = User.objects.filter(username = username, password= password).values().first()
    else: 
        data = Business.objects.filter(username = username, password= password).values().first()

    request.session['user'] = data
    return data

def forgot_password(request):

    if request.method == 'POST':
        form = ForgotPwdForm(request.POST)

        if(form.is_valid()):

            user = User.objects.filter(email = form.cleaned_data['email']).first()

            if user == None:
                form.add_error('email', "User not found , please check your email.")
                return render(request, 'forgot-password.html', {
                    "form": form,
                    "title": "Forgot Password - Quickfeed"
                })

            if((form.cleaned_data['password'] != form.cleaned_data['cnf_password'])):
                form.add_error('password', "Password does not match.")
                return render(request, 'forgot-password.html', {
                    "form": form,
                    "title": "Forgot Password - Quickfeed"
                })

            my_queryset = User.objects.filter(email = form.cleaned_data['email']).update(password= form.cleaned_data['password'])
            
            pprint({my_queryset: my_queryset})

            form = LoginForm()

            message = "Passoword has been changed successfully."
    
            return render(request, "login.html", {"form": form, "message": message})

        else:
            form.add_error('email', "User not found , please check your email.")
    else:
        form = ForgotPwdForm()

    return render(request, 'forgot-password.html', {
        "form": form,
        "title": "Forgot Password - Quickfeed"
    })