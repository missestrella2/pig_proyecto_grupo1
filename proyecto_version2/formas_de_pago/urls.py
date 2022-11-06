from django.urls import path
from . import views 

urlpatterns=[

    path('formas-de-pago/',views.formas_de_pago, name="formas_de_pago"),
    path('formas-de-pago/alta-medio-de-pago',views.alta_medio_de_pago, name="alta_medio_de_pago"),
    path('formas-de-pago/baja-medio-de-pago',views.baja_medio_de_pago, name="baja_medio_de_pago"),
]