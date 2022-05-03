from django.urls import path
from Viajes import views

urlpatterns = [
    path('padre', views.padre_template),
    path('crear-vehiculo', views.crear_vehiculos),
    path('crear-destino', views.crear_destino),
    path("mostrar-vehiculos", views.Vehiculos_vista.as_view(), name = "Mostrar_vehiculos"),
    path("mostrar-destinos", views.Destinos_vista.as_view(), name = "Mostrar_destinos"),
    path("mostrar-vuelos", views.Vuelos_vista.as_view(), name = "Mostrar_vuelos"),
    path("mostrar-tickets", views.Tickets_vista.as_view(), name = "Mostrar_tickets"),
    path('crear-ticket', views.crear_ticket, name = "Crear_ticket"),
    path("ticket-usuario", views.mostrar_tickets_astroturista, name = "Mostrar_tickets_usuario"),
    path("eliminar-vehiculo/<pk>", views.Vehiculos_delete.as_view(), name = "Eliminar_vehiculo"),
    path("eliminar-destino/<pk>", views.Destino_delete.as_view(), name = "Eliminar_destino"),
    path("editar-vehiculo/<pk>", views.Vehiculos_update.as_view(), name = "Editar_vehiculo"),
    path("editar-destino/<pk>", views.Destino_update.as_view(), name = "Editar_destino"),
    #path("crear-vuelo", views.crear_vuelo, name = "Crear_vuelo"),
    path("pagos", views.prueba_pagos),
    path("", views.inicio, name = "Inicio"),
    path("tickets-admin", views.ver_tickets_admin, name = "Tickets-admin"),
    path("editar-ticket-admin/<pk>", views.Ticket_admin_delete.as_view(), name = "Eliminar_admin_ticket"),
]