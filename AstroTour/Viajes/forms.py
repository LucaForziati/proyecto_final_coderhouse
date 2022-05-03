from django import forms
from django.contrib.auth.models import User

from .models import  Destino, Ticket_abordaje, Vehiculo, Vuelos_pasajeros, Vuelos
from Usuario.models import  Astroturista

class Vehiculo_formulario(forms.ModelForm):

    class Meta:

        model = Vehiculo
        fields = ("__all__")
        widgets = {
            'nombre_vehiculo':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre del vehiculo',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'cantidad_pasajeros':forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese cantidad de pasajeros del vehiculo',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'velocidad':forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese velocidad del vehiculo',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'precio_x_km':forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el precio por kilometro del vehiculo',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descripcion del vehiculo',
                    'cols': '2px',
                    'rows': '2px'
                }
            ),
        }

class Ticket_formulario(forms.ModelForm):

    class Meta:

        model = Ticket_abordaje
        fields = ('destino', 'vehiculo', 'fecha')
        widgets = {
            'fecha':forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
            'fecha':forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
        }


class Destino_formulario(forms.ModelForm):

    class Meta:

        model = Destino
        fields = ("__all__")
        widgets = {
            'lugar':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre del destino',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'ubicacion':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese ubicacion del destino',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'kilometros':forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese kilometros al destino (desde la tierra)',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'gravedad':forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese gravedad del destino',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descripcion del destino',
                    'cols': '2px',
                    'rows': '2px'
                }
            ),
        }

class Vuelos_pasajeros_formulario(forms.ModelForm):

    class Meta:

        model = Vuelos_pasajeros
        fields = ("__all__")

class Vuelos_formulario(forms.ModelForm):

    class Meta:

        model = Vuelos
        fields = ("__all__")