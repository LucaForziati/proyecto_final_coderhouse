from django.urls import path
from Comunidad import views

urlpatterns = [
    path('padre_comunidad', views.ver_padre_comunidad),
    path('crear-post', views.crear_post),
    path("posts", views.Post_vista.as_view(), name = "Mostrar_posts"),
]