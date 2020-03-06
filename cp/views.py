from django.shortcuts import render
from users.utils import obter_usuario_logado
# from django.contrib.auth.decorators import login_required
# @login_required(login_url='/users/login/')

def home(request):
    user = obter_usuario_logado(request)
    if user:
        print(user.nome)
    contexto = {'title':'Home', 'user':user}
    return render(request, 'index.html',contexto)