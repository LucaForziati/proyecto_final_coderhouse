from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class UserEditForm(UserCreationForm):


    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 


    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
        help_texts = {k:"" for k in fields}
    


class AstroturistaEditForm(Astroturista_formulario):

    pasaporte_espacial = forms.IntegerField(label = "Modifica tu pasaporte espacial")
    peso = forms.IntegerField(label = "Modifica tu peso")
    avatar = forms.ImageField( label = "Modifica tu avatar")


    class Meta:

        model = Astroturista
        fields = ('pasaporte_espacial','peso', 'avatar')
        help_texts = {k:"" for k in fields}