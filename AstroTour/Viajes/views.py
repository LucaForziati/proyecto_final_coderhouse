from email.message import EmailMessage
from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .models import  Destino, Ticket_abordaje, Vehiculo, Vuelos, Vuelos_pasajeros
from .forms import  Destino_formulario, Ticket_formulario, Vehiculo_formulario, Vuelos_formulario

from Usuario.models import Astroturista, Acompañantes

from django.views.generic import ListView

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from datetime import datetime

from django.contrib.auth.decorators import user_passes_test

from django.views.generic.edit import DeleteView, UpdateView

import qrcode

from django.conf import settings

from django.core.mail import send_mail

# Create your views here.

class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

def padre_template(request):
    
    return render(request, "padre_viaje.html")
    

def inicio(request):

    return render(request, "inicio.html")


@user_passes_test(lambda u: u.is_superuser)
def crear_vehiculos(request):

    if request.method == "POST":

        vehiculo_formulario = Vehiculo_formulario(request.POST, request.FILES)

        if vehiculo_formulario.is_valid():

            vehiculo_informacion = vehiculo_formulario.cleaned_data
            
            vehiculo = Vehiculo (
                nombre_vehiculo = vehiculo_informacion["nombre_vehiculo"],
                cantidad_pasajeros = vehiculo_informacion["cantidad_pasajeros"],
                velocidad = vehiculo_informacion["velocidad"],
                precio_x_km = vehiculo_informacion["precio_x_km"],
                imagen = vehiculo_informacion["imagen"],
                resumen = vehiculo_informacion["resumen"],
                descripcion = vehiculo_informacion["descripcion"]
                )
            vehiculo.save()

            vehiculo_contexto = vehiculo_informacion


            return render(request, "padre_viaje.html", {"vehiculo_contexto": vehiculo_contexto})

    else: 

        vehiculo_formulario = Vehiculo_formulario()

        return render(request, "crear_vehiculo.html", {"crear_vehiculo_formulario": vehiculo_formulario})

class Vehiculos_vista(ListView):

    model = Vehiculo
    template_name = "mostrar_vehiculos.html"



class Vehiculos_delete(DeleteView):

    model = Vehiculo
    success_url = "/viaje/mostrar-vehiculos"
    template_name = "mostrar_vehiculos.html"

class Vehiculos_update(UpdateView):

    model = Vehiculo
    success_url = "/viaje/mostrar-vehiculos"
    fields = ['nombre_vehiculo', 'cantidad_pasajeros', 'velocidad', 'precio_x_km', 'imagen', 'descripcion']
    template_name = "editar_vehiculo.html"

def ver_vehiculo(request, id):
        
    vehiculos = Vehiculo.objects.get(id=id)

    return render(request,'ver_vehiculo.html', {'vehiculos': vehiculos})



@user_passes_test(lambda u: u.is_superuser)
def crear_destino(request):

    if request.method == "POST":

        destino_formulario = Destino_formulario(request.POST, request.FILES)

        if destino_formulario.is_valid():

            destino_informacion = destino_formulario.cleaned_data
            
            destino = Destino (
                lugar = destino_informacion["lugar"],
                ubicacion = destino_informacion["ubicacion"],
                kilometros = destino_informacion["kilometros"],
                gravedad = destino_informacion["gravedad"],
                imagen = destino_informacion["imagen"],
                resumen = destino_informacion["resumen"],
                descripcion = destino_informacion["descripcion"]
                )
            destino.save()

            destino_contexto = destino_informacion

            return render(request, "padre.html", {"destino_contexto": destino_contexto})

    else: 

        destino_formulario = Destino_formulario()

        return render(request, "crear_destino.html", {"crear_destino_formulario": destino_formulario})


def ver_destino(request, id):
        
    destinos = Destino.objects.get(id = id)

    return render(request,'ver_destino.html', {'destinos': destinos})


class Destinos_vista(ListView):

    model = Destino
    template_name = "mostrar_destinos.html"

class Destino_delete(DeleteView):

    model = Destino
    success_url = "/viaje/mostrar-destinos"
    template_name = "mostrar_destinos.html"

class Destino_update(UpdateView):

    model = Destino
    success_url = "/viaje/mostrar-destinos"
    fields = ['lugar', 'ubicacion', 'kilometros', 'gravedad', 'imagen', 'descripcion']
    template_name = "editar_destino.html"

@login_required
def crear_ticket(request):

    user1 = request.user
    astroturista = Astroturista.objects.get(user = user1)


    if request.method == "POST":

        ticket_formulario = Ticket_formulario(request.POST)

        if ticket_formulario.is_valid():

            ticket_informacion = ticket_formulario.cleaned_data

            if ticket_informacion["fecha"] > datetime.now().date():
            
                ticket = Ticket_abordaje (
                    usuario = astroturista,
                    destino = ticket_informacion["destino"],
                    vehiculo = ticket_informacion["vehiculo"],
                    precio = None,
                    tiempo = None,
                    fecha = ticket_informacion["fecha"]
                    )
                ticket.save()
            
                ticket.precio = ticket.destino.kilometros * ticket.vehiculo.precio_x_km
                ticket.save()

                ticket.tiempo = ticket.destino.kilometros / ticket.vehiculo.velocidad
                ticket.save()


                tiempo = (ticket.tiempo*60) % 60   

                vuelos = Vuelos (   
                    destino = ticket_informacion["destino"],
                    vehiculo = ticket_informacion["vehiculo"],
                    fecha = ticket_informacion["fecha"],
                    asientos_disponibles = ticket.vehiculo.cantidad_pasajeros - 1,
                    tiempo_viaje = ticket.tiempo
                )
                
                if not Vuelos.objects.filter(fecha__icontains = ticket.fecha).exists(): 

                    vuelos.save()
                    vuelos.vuelo_ticket.add(ticket.id)

                elif Vuelos.objects.filter(fecha__icontains = ticket.fecha).exists() and (not Vuelos.objects.filter(vehiculo = ticket.vehiculo).exists() or not Vuelos.objects.filter(destino = ticket.destino).exists()): 

                    
                    vuelos.save()
                    vuelos.vuelo_ticket.add(ticket.id)

                else:
                    vuelo_ya_creado = Vuelos.objects.get(fecha = ticket.fecha, destino_id = ticket.destino)
                    Vuelos.objects.get(fecha = ticket.fecha, destino_id = ticket.destino).vuelo_ticket.add(ticket.id)
                    vuelo_ya_creado.asientos_disponibles -= 1
                    vuelo_ya_creado.save()
                
                
                ticket_contexto = ticket

                asunto_mail = f"Se ha generado el ticket de abordaje {ticket.id}"
                mensaje = f"¡Muchas gracias {astroturista}! Su vuelo se ha generado correctamente. Viste nuestro sitio web para mas informacion"
                email_from = settings.EMAIL_HOST_USER 
                recipent_list = [astroturista.email]
                send_mail(asunto_mail, mensaje, email_from, recipent_list)

                return render(request, "ticket_generado.html", {"ticket": ticket_contexto})
            
            else:
                
                ticket_formulario = Ticket_formulario()
                vehiculos = Vehiculo.objects.all()
                destinos = Destino.objects.all()

                mensaje_error = "Fecha no valida. Ingrese una fecha posterior al dia de doy"

                return render(request, "crear_ticket.html", {"crear_ticket_formulario": ticket_formulario, "vehiculos": vehiculos, "destinos": destinos, "mensaje_error": mensaje_error})

    else: 

        ticket_formulario = Ticket_formulario()
        vehiculos = Vehiculo.objects.all()
        destinos = Destino.objects.all()

        return render(request, "crear_ticket.html", {"crear_ticket_formulario": ticket_formulario, "vehiculos": vehiculos, "destinos": destinos})



class Tickets_vista(ListView, LoginRequiredMixin):

    model = Ticket_abordaje
    template_name = "mostrar_tickets.html"

class Ticket_admin_delete(DeleteView):

    model = Ticket_abordaje
    success_url = "/viaje/tickets-admin"
    template_name = "ver_tickets_admin.html"


class Vuelos_vista(SuperuserRequiredMixin, ListView):

    model = Vuelos
    template_name = "mostrar_vuelos.html"


@login_required
def mostrar_tickets_astroturista(request):

    user1 = request.user
    astroturista = Astroturista.objects.get(user = user1)
    now = datetime.now().date()
    print(now)

    tickets = Ticket_abordaje.objects.filter(usuario = astroturista)

    contexto = {"tickets_astrotusrita": tickets, "fecha_hoy": now}

    return render(request, "mostrar_ticket_usuario.html", contexto)

class Ticket_delete(DeleteView):

    model = Ticket_abordaje
    success_url = "/viaje/ticket-usuario"
    template_name = "mostrar_tickets_usuario.html"


def prueba_pagos(request):

    return render(request, "pagos.html")

@user_passes_test(lambda u: u.is_superuser)
def ver_tickets_admin(request):

    if request.method == "POST":
        id_ticket = request.POST["numero_ticket"]
        dato_ticket = Ticket_abordaje.objects.get(id = id_ticket)

        print("++++++++++")
        print(dato_ticket)

        ticket_contexto = dato_ticket

        return render(request, "ticket_buscado.html", {"ticket_contexto": ticket_contexto})
    else:
        


        tickets = Ticket_abordaje.objects.all()
        now = datetime.now().date()

        return render(request, "ver_tickets_admin.html", {"tickets": tickets, "fecha_hoy": now})






