from django.shortcuts import render, redirect
from django.contrib import messages
from.formulario import UserRegisterForm

def registro(request):
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data.get('username')
            messages.success(request, f'Sua conta foi criada com sucesso! Voce agora pode entrar.')
            return redirect('login')
    else:
        formulario = UserRegisterForm()
    return render(request, 'users/registro.html', {'form': formulario})

def profile():
    return render(request, 'users/profile.html')