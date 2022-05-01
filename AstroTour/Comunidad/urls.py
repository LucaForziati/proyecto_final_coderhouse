from django.urls import path
from Comunidad import views

urlpatterns = [
    path('padre_comunidad', views.ver_padre_comunidad),
    path('crear-post', views.crear_post, name = "Crear_posts"),
    path("posts/<id>", views.ver_posteos, name = "Mostrar_posts"),
    path("posteos", views.posteos, name = "Ver_post"),
    path("eliminar-comentario/<pk>", views.Comentario_delate.as_view(), name = "Eliminar_comentario"),
    path("eliminar-post/<pk>", views.Posts_delate.as_view(), name = "Eliminar_posteo"),
    path('likes/<id>', views.dar_like, name="Likes"),
]