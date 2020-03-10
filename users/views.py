from .form import FormUser
from .utils import obter_usuario_logado
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .form import LoginForm
from django.contrib.auth import logout
class register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('informacoes')
    template_name = 'users/register.html'

#cria as informações do usuario
def novo_user(request):
    if request.method == 'POST':
        form_user = FormUser(request.POST)
        if form_user.is_valid():
            post = form_user.save(commit=False)
            post.nome_usuario = request.user
            post.save()
            


    contexto = {'form':FormUser() }
    return render(request,'users/cadastra_usuaria.html',contexto)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                   password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                        
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def sair(request):
    logout(request)
    return redirect('index')

