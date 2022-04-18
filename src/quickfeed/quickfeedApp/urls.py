from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#url  configuration

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login', views.login, name='login-page'),
    path('register', views.register, name='register-page'),
    path('old', views.homepageold, name='oldhome')
]

urlpatterns += staticfiles_urlpatterns()