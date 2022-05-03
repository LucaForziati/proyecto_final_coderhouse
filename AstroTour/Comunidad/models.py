from django.db import models
from Usuario.models import Astroturista 
from django.utils import timezone

from django.conf import Settings,settings


# Create your models here.

class Posts(models.Model):

    usuario = models.ForeignKey(Astroturista, on_delete= models.CASCADE)
    nombre_post = models.CharField(max_length= 50)
    descripcion = models.CharField(max_length= 50)
    texto = models.TextField()
    imagen = models.ImageField(upload_to = "imagen")

    def get_like_count(self):
        return self.likes_set.all().count()

class Comentario(models.Model):

    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Astroturista, on_delete= models.CASCADE)
    comentario = models.CharField(max_length = 140)
    #created_date = models.DateTimeField(default=timezone.now())

class Likes(models.Model):
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Astroturista, on_delete= models.CASCADE)

    def __str__(self):
        return f'Like de: {self.usuario}, post= {self.post.titulo}'


