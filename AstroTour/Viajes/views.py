from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .models import  Destino, Ticket_abordaje, Vehiculo, Vuelos, Vuelos_pasajeros
from .forms import  Destino_formulario, Ticket_formulario, Vehiculo_formulario

from django.views.generic import ListView

# Create your views here.

def padre_template(request):

    return render(request, "padre_viaje.html")

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
                imagen = vehiculo_informacion["imagen"]
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
                imagen = destino_informacion["imagen"]
                )
            destino.save()

            destino_contexto = destino_informacion

            return render(request, "padre.html", {"destino_contexto": destino_contexto})

    else: 

        destino_formulario = Destino_formulario()

        return render(request, "crear_destino.html", {"crear_destino_formulario": destino_formulario})

class Destinos_vista(ListView):

    model = Destino
    template_name = "mostrar_destinos.html"
