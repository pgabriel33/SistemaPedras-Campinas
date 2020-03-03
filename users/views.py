from .form import FormUser
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm

def register_user(request):
    url = 'users/register.html'
    if request.method == 'POST':
        name_user = request.POST["username"]
        return novo_user(request,name_user)
    context = {'form':UserCreationForm()}
    return render(request, 'users/register.html',context)

#cria as informações do usuario
def novo_user(request,nome_user):
    try:
        a = User.objects.get(username=nome_user)
    except ObjectDoesNotExist:
        raise ValueError('Usuario Não Existe')

    if request.method == 'POST':
        form_user = FormUser(request.POST)
        if form_user.is_valid():
            post = form_user.save(commit=False)
            post.nome_usuario = request.user
            post.save()
            success = {'oi'}


    contexto = {'form':FormUser(), 'success':success  }
    return render(request,'users/cadastra_usuaria.html',contexto)

