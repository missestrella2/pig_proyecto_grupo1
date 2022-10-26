from django.urls import path 
from . import views
from django import forms


urlpatterns=[

    path('',views.index,name="login"), 
    path('login/login-form',views.login_form,name="login_form")
]