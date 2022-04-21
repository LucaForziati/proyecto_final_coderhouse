from django import forms
from django.contrib.auth.models import User

from .models import Astroturista, Acompañantes

#############################################

class Astroturista_formulario(forms.ModelForm):

    class Meta:

        model = Astroturista
        fields = ('pasaporte_espacial','peso', 'avatar')

class Acompañantes_formulario(forms.ModelForm):

    class Meta:

        model = Acompañantes
        fields = ('nombre', 'apellido', 'pasaporte_espacial','peso')