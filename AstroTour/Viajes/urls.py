from django.urls import path
from Viajes import views

urlpatterns = [
    path('padre', views.padre_template),
    path('crear-vehiculo', views.crear_vehiculos),
    path('crear-destino', views.crear_destino),
    path("mostrar-vehiculos", views.Vehiculos_vista.as_view(), name = "Mostrar_vehiculos"),
    path("mostrar-destinos", views.Destinos_vista.as_view(), name = "Mostrar_destinos"),
]