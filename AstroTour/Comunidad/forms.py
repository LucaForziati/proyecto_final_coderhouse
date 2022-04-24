from django import forms
from .models import Post


class Post_formulario(forms.ModelForm):

    class Meta:

        model = Post
        fields = ('nombre_post', 'descripcion', 'texto', 'imagen')