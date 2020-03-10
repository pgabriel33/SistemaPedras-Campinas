from django.shortcuts import render, redirect
from users.utils import obter_usuario_logado
# from django.contrib.auth.decorators import login_required
# @login_required(login_url='/users/login/')

def home(request):
    contexto = {'title':'Home', 'user':request.user.pk}
    # valida se exite algum usuario logado
    if request.user:
        # caso exista ele busca ele no usuario principal
        user = obter_usuario_logado(request)
        # obtem um retorno q pode ser um numero ID ou uma string vazia
        test_user =  user
        
    else:
        test_user = True

    contexto.update({'test':test_user})    
    return render(request, 'index.html',contexto)     
    