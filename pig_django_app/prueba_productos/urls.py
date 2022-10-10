from django.urls import path #segun clase 10
from . import views #segun clase 10 significa: desde donde estoy importa las vistas

urlpatterns=[

    path('productos/',views.vista_de_productos) #entra a la funcion vista_de_productos de las views de prueba productos 

]
