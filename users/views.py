from django.shortcuts import render, HttpResponse
from .form import FormUser
from django.contrib.auth.models import User

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'



# Create your views here.

def novo_user(request):
    if request.method == 'POST':
        form_user = FormUser(request.POST)
        print(form_user.errors)
        if form_user.is_valid():
            post = form_user.save(commit=False)
            post.nome_usuario = request.user
            post.save()
            return HttpResponse('haaaaaa')
    else:
        contexto = {'form':FormUser()  }
        return render(request,'users/cadastra_usuaria.html',contexto)

    return HttpResponse('oi')