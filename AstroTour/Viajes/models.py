from django.db import models
from Usuario.models import Astroturista 
from django.contrib.auth.models import User

import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# Create your models here.

class Destino(models.Model):

    lugar = models.CharField(max_length = 50)
    ubicacion = models.CharField(max_length= 50)
    kilometros = models.IntegerField()
    gravedad = models.FloatField()
    imagen = models.ImageField(upload_to = "imagen", null = True, blank = True)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.lugar}"

class Vehiculo(models.Model):

    nombre_vehiculo = models.CharField(max_length= 50)
    cantidad_pasajeros = models.IntegerField()
    velocidad = models.IntegerField()
    precio_x_km = models.IntegerField()
    imagen = models.ImageField(upload_to = "imagen", null = True, blank = True)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre_vehiculo}"

class Ticket_abordaje(models.Model):

    usuario = models.ForeignKey(Astroturista, on_delete= models.CASCADE)
    destino = models.ForeignKey(Destino, on_delete= models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete= models.CASCADE)
    precio = models.IntegerField(blank = True, null = True) 
    tiempo = models.FloatField(blank = True, null = True)
    fecha = models.DateField(blank = True, null = True)
    codigo_qr = models.ImageField(upload_to = "imagen", null = True, blank = True)

    def __str__(self):
        return f"Ticket Nº {self.id} - {self.usuario} "

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(f'Ticket id: {self.id}')
        canvas = Image.new('RGB', (290, 290), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.usuario}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.codigo_qr.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class Vuelos(models.Model):

    vuelo_ticket = models.ManyToManyField(Ticket_abordaje, through= "Vuelos_pasajeros", blank = True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete= models.CASCADE, blank = True, null = True)
    asientos_disponibles = models.IntegerField(blank = True, null = True)
    destino = models.ForeignKey(Destino, on_delete= models.CASCADE, blank = True, null = True)
    fecha = models.DateField(blank = True, null = True)
    tiempo_viaje = models.IntegerField(blank = True, null = True)


class Vuelos_pasajeros(models.Model):

    vuelos = models.ForeignKey(Vuelos, on_delete= models.CASCADE, blank = True, null = True)
    tickets = models.ForeignKey(Ticket_abordaje, on_delete= models.CASCADE, blank = True, null = True)
