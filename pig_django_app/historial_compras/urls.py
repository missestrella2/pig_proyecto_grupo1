from django.urls import path #segun clase 10
from . import views #segun clase 10 significa: desde donde estoy importa las vistas

urlpatterns=[

    path('historial-compras/',views.historial_compras,name="historial_compras"),
]