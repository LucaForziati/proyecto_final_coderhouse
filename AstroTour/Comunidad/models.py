from django.db import models
from Usuario.models import Astroturista 
from datetime import timezone


# Create your models here.

class Post(models.Model):

    usuario = models.ForeignKey(Astroturista, on_delete= models.CASCADE)
    nombre_post = models.CharField(max_length= 50)
    descripcion = models.CharField(max_length= 50)
    texto = models.TextField()
    imagen = models.ImageField(upload_to = "imagen", null = True, blank = True)

class Comentarios(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Astroturista, on_delete= models.CASCADE)
    comentario = models.CharField(max_length = 140)
    #created_date = models.DateTimeField(default=timezone.now())


