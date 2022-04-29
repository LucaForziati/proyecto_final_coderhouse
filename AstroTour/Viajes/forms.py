from django import forms
from django.contrib.auth.models import User

from .models import  Destino, Ticket_abordaje, Vehiculo, Vuelos_pasajeros, Vuelos
from Usuario.models import  Astroturista

class Vehiculo_formulario(forms.ModelForm):

    class Meta:

        model = Vehiculo
        fields = ("__all__")

class Ticket_formulario(forms.ModelForm):

    class Meta:

        model = Ticket_abordaje
        fields = ('destino', 'vehiculo', 'fecha')


class Destino_formulario(forms.ModelForm):

    class Meta:

        model = Destino
        fields = ("__all__")

class Vuelos_pasajeros_formulario(forms.ModelForm):

    class Meta:

        model = Vuelos_pasajeros
        fields = ("__all__")

class Vuelos_formulario(forms.ModelForm):

    class Meta:

        model = Vuelos
        fields = ("__all__")