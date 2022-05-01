from django.urls import path
from Usuario import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('padre', views.padre_template),
    path('login', views.login_request, name = "Login"),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name = 'login.html'), name = 'Logout'),
    path('editar', views.editar_perfil, name = 'Editar_perfil'),
    path('register-super', views.register_superusuario, name = 'Register_super'),
    path('perfil', views.perfil_propio, name = 'Perfil_propio'),
]