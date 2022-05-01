from django import forms
from .models import Comentario, Posts


class Post_formulario(forms.ModelForm):

    class Meta:

        model = Posts
        fields = ('nombre_post', 'descripcion', 'texto', 'imagen')

class Comentarios_formulario(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ("comentario",)
        label={
            'comentario': 'Comentario'
        }
        widgets = {
            'comentario':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su comentario',
                    'cols': '2px',
                    'rows': '2px'
                }
            )
        }