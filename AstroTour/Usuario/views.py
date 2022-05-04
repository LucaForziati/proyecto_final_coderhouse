from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from Viajes.models import Ticket_abordaje

from .models import Astroturista

from .forms import Astroturista_formulario, UserEditForm, AstroturistaEditForm, SuperUserCreationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.conf import settings

from django.core.mail import send_mail



# Create your views here.

@login_required
def padre_template(request):

    avatar = Astroturista.objects.get(user = request.user.id)

    return render(request, "padre.html", {'avatar': avatar.avatar.url})

def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contra)

            if user is not None:

                login(request, user)

                return render(request, "inicio.html", {"usuario": user})
            else:

                return render(request, "inicio.html")
        else:

            return render(request, "problemas_al_ingresar.html")

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

def register(request):

    if request.method == "POST":
   
        form = UserCreationForm(request.POST)
        astroturista_form = Astroturista_formulario(request.POST, request.FILES)

        if form.is_valid() and astroturista_form.is_valid():

            username = form.cleaned_data["username"]
            user = form.save()

            astroturista = astroturista_form.save(commit = False)
            astroturista.user = user
            astroturista.save()

            return render(request, "inicio.html")

    
    else:
   
        form = UserCreationForm()
        astroturista_form = Astroturista_formulario(request.POST)

    return render(request, "registro.html", {"form": form, "astroturista_form": astroturista_form})

class User_delete(DeleteView):

    model = User
    success_url = "/viaje/"
    template_name = "perfil.html"

def register_superusuario(request):
    

    if request.method == "POST":


        if request.POST["cod_ver"] == "24B42":
    
            form = SuperUserCreationForm(request.POST)
            astroturista_form = Astroturista_formulario(request.POST, request.FILES)
            
            if form.is_valid() and astroturista_form.is_valid():

                username = form.cleaned_data["username"]

                user = form.save()

                astroturista = astroturista_form.save(commit = False)
                astroturista.user = user
                astroturista.save()

                return render(request, "inicio.html")

            else:

                return render(request, "inicio.html")

        else:
            
            form = SuperUserCreationForm()

            return render(request, "registro_superusuario.html", {"form": form})

    else:
    
        form = SuperUserCreationForm()
        astroturista_form = Astroturista_formulario(request.POST)

        return render(request, "registro_superusuario.html", {"form": form, "astroturista_form": astroturista_form})

@login_required
def editar_perfil(request):

    usuario = request.user
    astroturista = Astroturista.objects.get(user = usuario)

    if request.method == 'POST':

        mi_formulario = UserEditForm(request.POST)
        mi_formulario2 = AstroturistaEditForm(request.POST, request.FILES)

        if mi_formulario.is_valid() and mi_formulario2.is_valid():

            informacion = mi_formulario.cleaned_data
            informacion2 = mi_formulario2.cleaned_data

            astroturista.pasaporte_espacial = informacion2['pasaporte_espacial']
            astroturista.nombre = informacion2['nombre']
            astroturista.apellido = informacion2['apellido']
            astroturista.email = informacion2['email']
            astroturista.peso = informacion2['peso']
            astroturista.avatar = informacion2['avatar']
            astroturista.save()

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()



            return render(request, "inicio_sesion.html")
    
    else:
        mi_formulario = UserEditForm()
        mi_formulario2 = AstroturistaEditForm()

        return render(request, "editar_perfil.html", {'mi_formulario': mi_formulario, 'usuario': usuario, 'astroturista': mi_formulario2})

@login_required
def perfil_propio(request):

    astroturista = Astroturista.objects.get(user = request.user)

    contexto = astroturista

    cantidad_viajes = Ticket_abordaje.objects.filter(usuario = astroturista).count()

    viajes_kilometros_acumulados = Ticket_abordaje.objects.filter(usuario = astroturista)
    kilometros_acumulados = 0

    for viaje in viajes_kilometros_acumulados:
        kilometros_acumulados += viaje.destino.kilometros
    

    return render(request, "perfil.html", {"astroturista": contexto, "cantidad_viajes": cantidad_viajes, "kilometros_acumulados": kilometros_acumulados})

@login_required
def perfil_astroturistas(request, id):

    perfil = Astroturista.objects.get(user = id)

    cantidad_viajes = Ticket_abordaje.objects.filter(usuario = perfil).count()

    viajes_kilometros_acumulados = Ticket_abordaje.objects.filter(usuario = perfil)
    kilometros_acumulados = 0

    for viaje in viajes_kilometros_acumulados:
        kilometros_acumulados += viaje.destino.kilometros
    
    return render(request,'perfil_astroturistas.html', {'perfil': perfil, "cantidad_viajes": cantidad_viajes, "kilometros_acumulados": kilometros_acumulados})


def contactanos(request):

    if request.method == "POST":

        email_contacto = request.POST["contacto_email"]
        nombre_contacto = request.POST["contacto_nombre"]
        apellido_contacto = request.POST["contacto_apellido"]
        texto_contacto = request.POST["contacto_texto"]

        asunto_mail = f"Se ha generado una consulta de {nombre_contacto} {apellido_contacto}"
        mensaje = f"{texto_contacto} --- Mail: {email_contacto}"
        email_from = email_contacto 
        recipent_list = ["astrotour2000@gmail.com"]
        send_mail(asunto_mail, mensaje, email_from, recipent_list)

        return render(request, "inicio.html")

    else: 

        return render(request, "contactenos.html")

def acerca(request):

    return render(request, "acerca.html")



