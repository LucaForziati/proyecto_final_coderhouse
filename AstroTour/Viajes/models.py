from django.db import models
from Usuario.models import Astroturista 
from django.contrib.auth.models import User
# Create your models here.

class Destino(models.Model):

    lugar = models.CharField(max_length = 50)
    ubicacion = models.CharField(max_length= 50)
    kilometros = models.IntegerField()
    gravedad = models.FloatField()
    imagen = models.ImageField(upload_to = "imagen", null = True, blank = True)

    def __str__(self):
        return f"{self.lugar}"

class Vehiculo(models.Model):

    nombre_vehiculo = models.CharField(max_length= 50)
    cantidad_pasajeros = models.IntegerField()
    velocidad = models.IntegerField()
    precio_x_km = models.IntegerField()
    imagen = models.ImageField(upload_to = "imagen", null = True, blank = True)

    def __str__(self):
        return f"{self.nombre_vehiculo}"

class Ticket_abordaje(models.Model):

    usuario = models.ForeignKey(Astroturista, on_delete= models.CASCADE)
    destino = models.ForeignKey(Destino, on_delete= models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete= models.CASCADE)
    precio = models.IntegerField(blank = True, null = True)
    tiempo = models.FloatField(blank = True, null = True)
    fecha = models.DateField(blank = True, null = True)

class Vuelos(models.Model):

    vuelo_ticket = models.ManyToManyField(Ticket_abordaje, through= "Vuelos_pasajeros")
    vehiculo = models.ForeignKey(Vehiculo, on_delete= models.CASCADE, blank = True, null = True)
    numero_pasajeros = models.IntegerField(blank = True, null = True)
    destino = models.ForeignKey(Destino, on_delete= models.CASCADE, blank = True, null = True)
    fecha = models.DateField(blank = True, null = True)

class Vuelos_pasajeros(models.Model):

    vuelos = models.ForeignKey(Vuelos, on_delete= models.CASCADE, blank = True, null = True)
    tickets = models.ForeignKey(Ticket_abordaje, on_delete= models.CASCADE, blank = True, null = True)
