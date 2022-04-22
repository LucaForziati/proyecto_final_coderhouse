from django.contrib import admin

from .models import Destino, Vehiculo, Ticket_abordaje, Vuelos, Vuelos_pasajeros

# Register your models here.

class Vuelos_pasajerosInLine(admin.TabularInline):
    model = Vuelos_pasajeros
    extra = 1


class Vuelosadmin(admin.ModelAdmin):

    inlines = [Vuelos_pasajerosInLine,]
    list_display = ("vehiculo", "destino", "fecha")

admin.site.register(Destino)
admin.site.register(Vehiculo)
admin.site.register(Ticket_abordaje)
admin.site.register(Vuelos, Vuelosadmin)
