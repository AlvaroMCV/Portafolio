from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Envio
from .forms import EnvioForm  # Necesitarás crear un formulario para crear nuevos envíos
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def search_shipment(request):
    # Lógica para buscar un envío por número de seguimiento u otros criterios
    if request.method == 'POST':
        numero_seguimiento = request.POST.get('numero_seguimiento')
        envio = Envio.objects.filter(numero_seguimiento=numero_seguimiento).first()
        if envio:
            return render(request, 'delivery/search_shipment.html', {'envio': envio})
        else:
            error_message = 'Envío no encontrado.'
            return render(request, 'delivery/search_shipment.html', {'error_message': error_message})
    return render(request, 'delivery/search_shipment.html')

@login_required
def new_shipment(request):
    if request.method == 'POST':
        form = EnvioForm(request.POST)
        if form.is_valid():
            envio = form.save(commit=False)
            envio.remitente = request.user
            envio.save()
            messages.success(request, 'Envío creado exitosamente.')
            return redirect('myshipments')
    else:
        form = EnvioForm()

    return render(request, 'delivery/new_shipment.html', {'form': form})


@login_required
def my_shipments(request):
    shipments = Envio.objects.filter(remitente=request.user)
    return render(request, 'delivery/my_shipments.html', {'shipments':shipments})

@login_required
def send_money(request):
    return render(request, 'delivery/money_sending.html')