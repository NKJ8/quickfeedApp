from pickle import FALSE, TRUE
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from .forms import ForgotPwdForm, LoginForm, SignUpForm, SignUpFormBusiness, UpdateProfileForm
from django.http import HttpResponse, HttpResponseRedirect
import re
from .models import User, Business

from pprint import pprint






# Create your views here.
# request handler
# Action


def homepage(request):

    # getting all the businesses
    business = Business.objects.order_by('review_count').values().reverse()[:5]
    return render(request, "index.html", {"title": "Welcome to quickfeed", 'business': business})

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
            #print("----",form.keys)
           
            # return
            if('user' in data.keys() and data['user'] != None):
                # get user data and send on profile page
                data = set_session(request, form.cleaned_data['username'], form.cleaned_data['password'])
                
                return render(request, 'user-profile.html', {
                    "data": data,
                    "form": UpdateProfileForm()
                })
            if( 'business' in data.keys() and data['business'] != None):
                # get user data and send on profile page
                data = set_session(request, form.cleaned_data['username'], form.cleaned_data['password'], False)

                #request.session['email'] = email
                return render(request, 'business-profile.html', {
                    "data": data,
                    "form": UpdateProfileForm()
                })
                return HttpResponse(request.POST.items())

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

                    data = set_session(request, form.cleaned_data['username'], form.cleaned_data['password'])

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
        form = SignUpFormBusiness(request.POST,request.FILES)

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
                        name = form.cleaned_data['name'],
                        image1 = form.cleaned_data['image1'],
                        image2 = form.cleaned_data['image2'],
                        image3 = form.cleaned_data['image3'],
                        image4 = form.cleaned_data['image4'],
                        image5 = form.cleaned_data['image5'],
                        image6 = form.cleaned_data['image6'],
                        )
                    business.save()

                    data = set_session(request, form.cleaned_data['username'], form.cleaned_data['password'], False)
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
    
    if(request.session['is_service_provider'] == 1) :
        return render(request, 'business-profile.html', {
            "data": data
        })
    

    return render(request, 'user-profile.html', {
        "data": data
    })

def service_details(request, service):

    data = {
        1 : {
           "name":  "Auto Repair",
           "images": ["https://dcba.lacounty.gov/wp-content/uploads/2017/10/CarRepairs.jpg", "https://www.thurstontalk.com/wp-content/uploads/2019/11/Boss-Auto-Repair-in-Olympia-Four-Wheel-Drive-Repair.jpg", "https://www.aaa.com/AAA/common/AAR/images/aar-main-image.jpg", "https://creditkarma-cms.imgix.net/wp-content/uploads/2019/04/auto-repair-financing_1010055706.jpg", "https://lensautomotive.com/wp-content/uploads/sites/309/2016/09/slider-blue.jpg"],
           "ratings": "0 ratings",
           "reviews": "0 reviews",
           "price": "200",
           "description": "Suspendisse quos? Tempus cras iure temporibus? Eu laudantium cubilia sem sem! Repudiandae et! Massa senectus enim minim sociosqu delectus posuere.",
           "tags": "",
           "business": "akshayb789"
        },
        2 : {
           "name":  "Plumbing",
           "images": "https://www.nutraingredients-usa.com/var/wrbm_gb_food_pharma/storage/images/9/4/5/8/218549-6-eng-GB/Akay-Flavours-Aromatics-Pvt.-Ltd2.jpg",
           "ratings": "0 ratings",
           "reviews": "0 reviews",
           "price": "200",
           "description": "Suspendisse quos? Tempus cras iure temporibus? Eu laudantium cubilia sem sem! Repudiandae et! Massa senectus enim minim sociosqu delectus posuere.",
           "tags": ""
        }
    }

    print("---------------------------------------------------------service", data[1]['images'][0])
    # return
    # user = request.session['user']
    return render(request, 'service-details.html', {
        "details": data[1]
    })


def update_user_profile(request):
    form = request.POST
    errors = {}
    success = ""
    data = {}
    if request.method == 'POST':

            if(form['name'].strip() == ""):
                errors['name'] = "Name is required"
            
            if(form['phone'].strip() == ""):
                errors['phone'] = "Phone is required"
            
            if(form['state'].strip() == ""):
                errors['state'] = "State is required"
            
            if(form['zipcode'].strip() == ""):
                errors['zipcode'] = "Zipcode is required"
            
            if(form['dob'].strip() == ""):
                errors['dob'] = "Date of birth is required"

            if(form['city'].strip() == ""):
                errors['city'] = "City is required"

            if(form['email'].strip() == ""):
                errors['email'] = "Email is required"

            if(form['address'].strip() == ""):
                errors['address'] = "Address is required"
            

            print("Errors", errors)
            print("Sesssion", request.session['user'])


            if(len(errors) == 0):
                # search the user in DB
                id = request.session['user']['id']
                user = User.objects.get(id = id)
                # update the user details and then save user
                user.dob = form['dob']
                user.email = form['email']
                user.name = form['name']
                user.phone = form['phone']
                user.state = form['state']
                user.zipcode = form['zipcode']
                user.city = form['city']
                user.address = form['address']
                user.save()

                success = "Data has been updated successfully."
                data = set_session(request, request.session['user_name'], request.session['password'], True)
                # return errors and success messages
            else:
                data = form

            print("Username", request.session['user_name'])
            print("Password", request.session['password'])
            
            return render(request, 'user-profile.html', {
                "data": data,
                "errors": errors,
                "success": success
            })

            
def update_business_profile(request):
    form = request.POST
    errors = {}
    success = ""
    data = {}
    if request.method == 'POST':

            if(form['name'].strip() == ""):
                errors['name'] = "Name is required"
            
            if(form['phone'].strip() == ""):
                errors['phone'] = "Phone is required"
            
            if(form['state'].strip() == ""):
                errors['state'] = "State is required"
            
            if(form['zipcode'].strip() == ""):
                errors['zipcode'] = "Zipcode is required"
            
            if(form['is_open'].strip() == ""):
                errors['is_open'] = "Business status is required"

            if(form['city'].strip() == ""):
                errors['city'] = "City is required"

            if(form['email'].strip() == ""):
                errors['email'] = "Email is required"

            if(form['address'].strip() == ""):
                errors['address'] = "Address is required"
                
            if(form['description'].strip() == ""):
                errors['description'] = "Description is required"
            

            print("Errors", errors)
            print("Sesssion", request.session['user'])


            if(len(errors) == 0):
                # search the user in DB
                id = request.session['user']['id']
                user = Business.objects.get(id = id)
                # update the user details and then save user
                user.is_open = form['is_open']
                user.email = form['email']
                user.name = form['name']
                user.phone = form['phone']
                user.state = form['state']
                user.zipcode = form['zipcode']
                user.city = form['city']
                user.address = form['address']
                user.description = form['description']
               # user.image1 = form['image1']
                user.save()

                success = "Data has been updated successfully."
                data = set_session(request, request.session['user_name'], request.session['password'], False)
                # return errors and success messages
            else:
                data = form

            print("Username", request.session['user_name'])
            print("Password", request.session['password'])
            
            return render(request, 'business-profile.html', {
                "data": data,
                "errors": errors,
                "success": success
            })


def set_session(request, username, password, user=True):
    data = {}
    request.session['is_logged_in'] = True
    if(user == True):
        data = User.objects.filter(username = username, password= password).values().first()
        request.session['is_service_provider'] = 0
    else: 
        data = Business.objects.filter(username = username, password= password).values().first()
        request.session['is_service_provider'] = 1

    request.session['user_name'] = username
    request.session['password'] = password
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
    
def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        business = Business.objects.filter(name__contains=searched)
        if not business:
            return render(request,'search_not_found.html',{'searched':searched,'business':business})
        else:
            return render(request,'search.html',{'searched':searched,'business':business})
    else:
        return render(request,'search.html')
    
    
def service_details(request):
    if request.method == "POST":
        searched = request.POST.get('Cat_val')
        business = Business.objects.filter(category_id__contains=searched).order_by('-review_count')
        if not business:
            return render(request,'search_not_found.html',{'searched':searched,'business':business})
        else:
            return render(request,'search_cat.html',{'searched':searched,'business':business})
    else:
        return render(request,'search.html')    