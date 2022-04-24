from django.shortcuts import render
from .forms import Post_formulario
from .models import Post
from Usuario.models import Astroturista
from django.views.generic import ListView

# Create your views here.

def ver_padre_comunidad(request):

    return render(request, "padre_comunidad.html")

def crear_post(request):

    user1 = request.user
    astroturista = Astroturista.objects.get(user = user1)

    if request.method == "POST":

        post_form = Post_formulario(request.POST, request.FILES)

        if post_form.is_valid():

            post_informacion = post_form.cleaned_data
            
            post = Post (
                usuario = astroturista,
                nombre_post = post_informacion["nombre_post"],
                descripcion = post_informacion["descripcion"],
                texto = post_informacion["texto"],
                imagen = post_informacion["imagen"],
                )
            post.save()

            post_contexto = post_informacion

            return render(request, "padre_comunidad.html", {"destino_contexto": post_contexto})

    else: 

        post_form = Post_formulario()

        return render(request, "crear_entrada.html", {"crear_entrada_formulario": post_form})

class Post_vista(ListView):

    model = Post
    template_name = "posts.html"