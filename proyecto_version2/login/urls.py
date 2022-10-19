from django.urls import path #segun clase 10
from . import views #segun clase 10 significa: desde donde estoy importa las vistas

urlpatterns=[

    path('',views.index,name="login") #entra a la funcion index de las views de "login"

]