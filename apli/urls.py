from django.urls import path
from . import views

app_name = "apli"
urlpatterns = [
    path("", views.VistaPrincipal, name="index"),
    path("kk", views.VistaResultados, name="prueba"),
]
