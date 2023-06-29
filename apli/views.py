from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import cliente
# Create your views here.


def VistaPrincipal(request):
    if request.method == 'GET':
      lista=cliente.objects.order_by('id')
      contexto={"lista":lista}
      return render(request, "index.html", contexto)
    
    else:
      lista=cliente.objects.order_by('id')
      contexto={"lista":lista}
      cliente.objects.create(name=request.POST['nombre'], last_name=request.POST['apellido'], cereal=request.POST['tamaño'] )
      return render(request, "index.html", contexto )




def VistaResultados(request):
    return render(request, 'Grafica.html')