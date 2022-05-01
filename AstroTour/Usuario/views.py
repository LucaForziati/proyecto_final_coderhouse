from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .models import Astroturista

from .forms import Astroturista_formulario, UserEditForm, AstroturistaEditForm, SuperUserCreationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



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

                return render(request, "inicio_sesion.html", {"usuario": user})
            else:

                return render(request, "inicio_sesion.html")
        else:

            return render(request, "inicio_sesion.html")

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

            return render(request, "login.html")

    
    else:
   
        form = UserCreationForm()
        astroturista_form = Astroturista_formulario(request.POST)

    return render(request, "registro.html", {"form": form, "astroturista_form": astroturista_form})

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

                return render(request, "login.html")

            else:

                return render(request, "login.html")

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


def perfil_propio(request):

    astroturista = Astroturista.objects.get(user = request.user)

    contexto = astroturista

    return render(request, "perfil.html", {"astroturista": contexto})

