from django.urls import path 
from . import views
from django import forms


urlpatterns=[

    path('',views.index,name="index"), 
    path('indexform/',views.indexform,name="indexform"), 
    path('paginaenblanco2/',views.paginaenblanco2,name="paginaenblanco2"), 
]