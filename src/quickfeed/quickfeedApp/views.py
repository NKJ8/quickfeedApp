from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
<<<<<<< HEAD
from .forms import SignUpForm
from django.http import HttpResponse

=======
from .forms import LoginForm, SignUpForm
from django.http import HttpResponse, HttpResponseRedirect

from .models import User
>>>>>>> b9f63482cd25e1680f9554b82036fb71668db625

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
            data['user'] = User.objects.filter(email = form.cleaned_data['email'], password= form.cleaned_data['password']).values().first()

            if(data['user']):
                # get user data and send on profile page
                return render(request, 'user-profile.html', {
                    "data": data['user']
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
            user = User(
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password']
            )
            user.save()
            return render(request, 'thank-you.html', {"title": "Thank you for registration"})
        else:
            form.add_error('cnf_password', "Please confirm password correctly")
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {
        "form": form,
        "title": "Signup - Quickfeed"
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



