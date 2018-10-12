from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data.get('username')
            messages.success(request, f'Parabens {username}! Conta criada com sucesso!')
            return redirect('blog-home')
    else:
        formulario = UserCreationForm()
    return render(request, 'users/registro.html', {'form': formulario})