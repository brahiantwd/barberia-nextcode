from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('base/', views.base, name='base'),
    path('clientes/', views.clientes, name='clientes'),
]