from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name='clientes'),
    path('atualiza_cliente/', views.att_cliente, name='att_cliente'),
]
