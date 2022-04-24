from django.urls import path, re_path, include

from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#url  configuration

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login', views.login, name='login-page'),
    path('signup', views.signup, name='signup-page'),
    path('old', views.homepageold, name='oldhome'),
    # path('login', views.login, name='login-page'),
    # path('thank-you', views.)
    # re_path(r'^login/$', views.login,  name='login-page'),
    #re_path(r'^logout/$', views.logout, name='logout'),
    # re_path(r'^signup/$', views.signup, name='signup-page'),
]

urlpatterns += staticfiles_urlpatterns()