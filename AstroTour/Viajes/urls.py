from django.urls import path
from Viajes import views

urlpatterns = [
    path('padre', views.padre_template),
    path('crear-vehiculo', views.crear_vehiculos),
]