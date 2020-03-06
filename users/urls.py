from . import views
from django.urls import path

urlpatterns = [
    path('cadastra/', views.register.as_view(),name='cadastra'),
    path('informacoes/<nome_user>/', views.novo_user,name='informacoes'),
    path('login/',views.user_login, name='login'),
    # path('logout/',views.logout, name='logout')
   
]