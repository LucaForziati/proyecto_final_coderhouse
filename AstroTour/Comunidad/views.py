from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Post_formulario, Comentarios_formulario
from .models import Posts, Comentario, Likes
from Usuario.models import Astroturista
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView

from django.contrib.auth.decorators import login_required

# Create your views here.

def ver_padre_comunidad(request):

    return render(request, "padre_comunidad.html")

@login_required
def crear_post(request):

    user1 = request.user
    astroturista = Astroturista.objects.get(user = user1)

    if request.method == "POST":

        post_form = Post_formulario(request.POST, request.FILES)

        if post_form.is_valid():

            post_informacion = post_form.cleaned_data
            
            post = Posts (
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

@login_required
def crear_comentario(request):

    user1 = request.user
    astroturista = Astroturista.objects.get(user = user1)

    if request.method == "POST":

        comentario_form = Comentarios_formulario(request.POST)

        if comentario_form.is_valid():

            comentario_informacion = comentario_form.cleaned_data
            
            comentario = Comentario (
                author = astroturista,
                #post = post_informacion["nombre_post"],
                comentario = comentario_informacion["texto"],
                )
            comentario.save()

            comentario_contexto = comentario_informacion

            return render(request, "padre_comunidad.html", {"destino_contexto": comentario_contexto})

    else: 

        comentario_form = Comentarios_formulario()

        return render(request, "posts.html", {"comentario_formulario": comentario_form})

@login_required
def posteos(request):
    post = Posts.objects.all()

    contexto={
        'post': post,
        'posteos': posteos
    }

    return render(request, 'inicio_posts.html', contexto)

@login_required
def ver_posteos(request, id):
        
    post = Posts.objects.get(id=id)
    comentario= Comentario.objects.filter(post__id = id)
    user1 = request.user
    astroturista = Astroturista.objects.get(user = user1)

    if request.method == "POST":
        form_comentario = Comentarios_formulario(request.POST)
        if request.user.is_authenticated:
            if form_comentario.is_valid:
                comentarioNuevo = form_comentario.save(commit=False)
                comentarioNuevo.author = astroturista
                comentarioNuevo.post = post
                comentarioNuevo.save()

    else:
        form_comentario = Comentarios_formulario()
    return render(request,'posts.html', {'post':post, 'comentario':comentario, 'form_comentario': form_comentario, 'astroturista': astroturista})

class Comentario_delate(DeleteView):

    model = Comentario
    success_url = "/comunidad/posteos"
    template_name = "posts.html"

class Posts_delate(DeleteView):

    model = Posts
    success_url = "/comunidad/posteos"
    template_name = "posts.html"

class Posts_update(UpdateView):

    model = Posts
    success_url = "/comunidad/posteos"
    fields = ['nombre_post', 'descripcion', 'texto', 'imagen']
    template_name = "editar_post.html"

@login_required
def dar_like(request,id):

    user1 = request.user
    astroturista = Astroturista.objects.get(user = user1)  

    post = Posts.objects.get(id=id)
    likes = Likes.objects.filter(usuario=astroturista, post=post)
    if likes.exists():
        likes.delete()
        return redirect('Mostrar_posts', id=id)
    Likes.objects.create(usuario=astroturista, post=post)
    return redirect('Mostrar_posts', id=id)
