from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='perfiles/', null=True, blank=True)

    def __str__(self):
        return self.usuario.username
