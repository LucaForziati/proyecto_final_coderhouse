from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Astroturista(models.Model):

    peso = models.IntegerField(null = True, blank = True)
    pasaporte_espacial = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = "avatares", null = True, blank = True)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Acompañantes(models.Model):

    astroturista = models.ForeignKey(Astroturista, on_delete= models.CASCADE)
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    pasaporte_espacial = models.IntegerField()
    peso = models.IntegerField(null = True, blank = True)
