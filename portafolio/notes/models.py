from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Nota(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    importante = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo