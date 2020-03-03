from . import views
from django.urls import path

urlpatterns = [
    path('cadastra/', views.register_user,name='cadastra'),
    path('informacoes/<nome_user>/', views.novo_user,name='informacoes'),
   
]