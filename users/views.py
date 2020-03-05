from .form import FormUser
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'users/register.html'

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



    contexto = {'form':FormUser() }
    return render(request,'users/cadastra_usuaria.html',contexto)

