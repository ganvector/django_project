from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def registro(request):
    formulario = UserCreationForm()
    return render(request, 'users/registro.html', {'form': formulario})