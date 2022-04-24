from django.db import models
from Usuario.models import Astroturista 

# Create your models here.

class Post(models.Model):

    usuario = models.ForeignKey(Astroturista, on_delete= models.CASCADE)
    nombre_post = models.CharField(max_length= 50)
    descripcion = models.CharField(max_length= 50)
    texto = models.TextField()
    imagen = models.ImageField(upload_to = "imagen", null = True, blank = True)


