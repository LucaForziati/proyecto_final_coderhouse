from django import forms
from .models import Comentario, Posts


class Post_formulario(forms.ModelForm):

    class Meta:

        model = Posts
        fields = ('nombre_post', 'descripcion', 'texto', 'imagen')
        widgets = {
            'texto':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su comentario',
                    'cols': '2px',
                    'rows': '2px'
                }
            ),
            'nombre_post':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre post',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descripcion del post',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
        }
        

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