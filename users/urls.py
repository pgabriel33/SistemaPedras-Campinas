from . import views
from django.urls import path

urlpatterns = [
    path('cadastra/', views.register.as_view(),name='cadastra'),
    path('informacoes/<nome_user>/', views.novo_user,name='informacoes'),
   
]