import uuid
from django.db import models

ESTADOS_ENVIOS = (
    ('pendiente', 'Pendiente'),
    ('en_transito', 'En tránsito'),
    ('entregado', 'Entregado'),
    ('devuelto', 'Devuelto'),
    ('cancelado', 'Cancelado'),
)

class Envio(models.Model):
    numero_seguimiento = models.CharField(max_length=50, unique=True, editable=False)
    remitente = models.CharField(max_length=255)
    destinatario = models.CharField(max_length=255, null=False, blank=False)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    direccion_destino = models.CharField(max_length=255, blank=False, null=False)
    valor_declarado = models.IntegerField(blank=False)
    estado = models.CharField(max_length=50, choices=ESTADOS_ENVIOS, default='pendiente')
    # Otros campos según tus necesidades

    def save(self, *args, **kwargs):
        if not self.numero_seguimiento:
            self.numero_seguimiento = str(uuid.uuid4()).replace('-', '').upper()[:12]
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Envío {self.numero_seguimiento}'

class Paquete(models.Model):
    envio = models.ForeignKey(Envio, related_name='paquetes', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    # Otros campos según tus necesidades

class EstadoEnvio(models.Model):
    envio = models.ForeignKey(Envio, related_name='estados', on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, choices=ESTADOS_ENVIOS)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()

    def __str__(self):
        return f'Estado {self.estado} de envío {self.envio.numero_seguimiento}'
