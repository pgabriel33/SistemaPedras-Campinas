from . import views
from django.urls import path

urlpatterns = [
    path('cadastra/', views.register.as_view(),name='cadastra'),
    path('informacoes/', views.novo_user,name='informacoes'),
    path('login/',views.user_login, name='login'),
    # path('logout/',views.logout, name='logout')
   
]