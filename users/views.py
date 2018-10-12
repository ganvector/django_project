from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
    else:
        formulario = UserCreationForm()
    return render(request, 'users/registro.html', {'form': formulario})