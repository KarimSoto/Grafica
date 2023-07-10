from django.urls import path
from . import views

app_name = "apli"
urlpatterns = [
    path("", views.VistaPrincipal, name="index"),
    path("resultados", views.VistaResultados, name="prueba"),
    path("prueba", views.prueba),
    path("lista", views.ListaClientes.as_view(), name='clientes')
]
