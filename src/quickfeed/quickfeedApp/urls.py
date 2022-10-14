
from django.urls import path, re_path, include

from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#url  configuration

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about-us', views.about_us, name='about-us-page'),
    path('login', views.login, name='login-page'),
    path('signup', views.signup, name='signup-page'),
    path('signupbusiness', views.signupbusiness, name='signup-page-business'),
    path('old', views.homepageold, name='oldhome'),
    path('logout-user', views.logout, name='logout-user'),
    path('user-profile-update', views.update_user_profile, name='update-user-profile'),
    path('business-profile-update', views.update_business_profile, name='update-business-profile'),
    path('service-details/<int:service>', views.service_details, name='service-details'),

    path('profile', views.profile, name='profile-page'),
    
    path('forgot-password', views.forgot_password, name='forgot-password-page'),
    # path('thank-you', views.)
    # re_path(r'^login/$', views.login,  name='login-page'),
    #re_path(r'^logout/$', views.logout, name='logout'),
    # re_path(r'^signup/$', views.signup, name='signup-page'),
]

urlpatterns += staticfiles_urlpatterns()