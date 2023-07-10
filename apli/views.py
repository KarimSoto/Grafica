from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic import *
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
    labels = []
    data = []
    queryset = cliente.objects.order_by('id')

    count_small = queryset.filter(cereal='S').count()
    count_medium = queryset.filter(cereal='M').count()
    count_large = queryset.filter(cereal='L').count()
    count_jumbo = queryset.filter(cereal='J').count()

    labels = ['Small', 'Medium', 'Large', 'Jumbo']
    data = [count_small, count_medium, count_large, count_jumbo]

    return render(request, 'Grafica.html', {'labels': labels, 'data': data})



def prueba(request):
  palabra=89
  return HttpResponse("hola"+palabra)


class Error404(TemplateView):
   template_name="Error_404.html"


class Error500(TemplateView):
   template_name="Error_500.html"

   @classmethod
   def as_error_view(cls):
      v=cls.as_view()
      def view(request):
         r=v(request)
         r.render()
         return r
      return view


class ListaClientes(ListView):
    model=cliente
    context_object_name ='clientes'
    template_name="listaClientes.html"