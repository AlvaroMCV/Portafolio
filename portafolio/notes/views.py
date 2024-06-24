from django.shortcuts import render, redirect
from .models import Nota
from .forms import NotaForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def my_notes(request):
    notes = Nota.objects.filter(autor=request.user)
    return render(request, 'notes/my_notes.html', {'notes':notes})


@login_required
def new_note(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.autor = request.user
            nota.save()
            return redirect('mynotes') 
    else:
        form = NotaForm()
    return render(request, 'notes/new_note.html', {'form': form})

def on_contruction(request):
    return render(request, 'common/on_construction.html')