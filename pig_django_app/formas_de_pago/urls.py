from django.urls import path #segun clase 10
from . import views #segun clase 10 significa: desde donde estoy importa las vistas

urlpatterns=[

    path('formas-de-pago/',views.formas_de_pago, name="formas_de_pago"),
]