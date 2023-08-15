from django.db import models
from django.contrib.auth.models import User


class Personas(models.Model):
    correo = models.CharField(primary_key=True, max_length=100)
    Run = models.PositiveIntegerField(unique=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    tipoUsuario = models.BooleanField()
    idUser = models.OneToOneField(User, models.CASCADE)
    
    def __str__(self):
        return self.nombre +' '+ self.apellido