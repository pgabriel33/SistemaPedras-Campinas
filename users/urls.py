from . import views
from django.urls import path

urlpatterns = [
    path('test/', views.register.as_view(),name='novo_'),
    path('te/', views.novo_user,name='novo_user'),
   
]