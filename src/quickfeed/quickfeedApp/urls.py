from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#url  configuration

urlpatterns = [
    path('homepage/', views.homepage)
]

urlpatterns += staticfiles_urlpatterns()