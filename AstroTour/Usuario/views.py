from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.

def padre_template(request):

    return render(request, "padre.html")

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
        astronauta_form = Astronauta_formulario(request.POST)

        if form.is_valid() and astronauta_form.is_valid():

            username = form.cleaned_data["username"]
            user = form.save()

            astronauta = astronauta_form.save(commit = False)
            astronauta.user = user
            astronauta.save()

            
            #print(form.cleaned_data[])
            return render(request, "index.html")

    
    else:

        form = UserCreationForm()
        astronauta_form = Astronauta_formulario()

    return render(request, "registro.html", {"form": form, "astronauta": astronauta_form})