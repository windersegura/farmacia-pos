from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from applications.inventario.models import Marca, Producto, Presentacion

# Create your views here.

class CreateMarcaView(CreateView):
    model = Marca
    template_name = 'inventario/marca/create-marca.html'
    fields = ('codigo', 'numero', 'nombre', 'descripcion')
