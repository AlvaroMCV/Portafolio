# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField(blank=False, null=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return f'Comentario de {self.autor.username} en {self.post.titulo}'