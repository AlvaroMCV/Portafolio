from django import forms
from .models import Envio, Paquete

class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ['descripcion', 'peso']

class EnvioForm(forms.ModelForm):
    destinatario = forms.CharField(label="Destinatario")
    descripcion_paquete = forms.CharField(label="Descripción del paquete")
    peso_paquete = forms.DecimalField(label="Peso del paquete", max_digits=5, decimal_places=2)

    class Meta:
        model = Envio
        exclude = ['numero_seguimiento', 'remitente', 'estado']
        fields = ['destinatario', 'direccion_destino', 'valor_declarado']  # Excluimos 'estado'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['estado'] = 'pendiente'  # Valor inicial de 'estado'

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.remitente = user.username
        if commit:
            instance.save()

            # Crear y asociar el paquete al envío
            paquete = Paquete(
                envio=instance,
                descripcion=self.cleaned_data['descripcion_paquete'],
                peso=self.cleaned_data['peso_paquete']
            )
            paquete.save()

        return instance
