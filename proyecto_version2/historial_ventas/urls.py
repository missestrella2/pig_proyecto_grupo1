from django.urls import path #segun clase 10
from . import views #segun clase 10 significa: desde donde estoy importa las vistas
from django.contrib.auth.decorators import login_required

urlpatterns=[

    path('historial-ventas/',login_required(views.historial_ventas),name="historial_ventas"),
   
]