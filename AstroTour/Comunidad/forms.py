from django import forms
from .models import Comentarios, Post


class Post_formulario(forms.ModelForm):

    class Meta:

        model = Post
        fields = ('nombre_post', 'descripcion', 'texto', 'imagen')

class Comentarios_formulario(forms.ModelForm):

    class Meta:
        model = Comentarios
        fields = ("__all__")