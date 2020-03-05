from django.shortcuts import render

def home(request):
    contexto = {'title':'Home'}
    return render(request, 'index.html',contexto)