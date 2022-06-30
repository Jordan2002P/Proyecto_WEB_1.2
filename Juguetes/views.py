

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
 
from .models import Producto
from .forms import ProductoForm
# Create your views here.
# las importaciones para la API  
from rest_framework import generics 
from .serializers import ProductoSerializer 


class API_objects(generics.ListCreateAPIView): 
    queryset = Producto.objects.all() 
    serializer_class = ProductoSerializer 


class API_objects_details(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Producto.objects.all() 
    serializer_class = ProductoSerializer 
 
class ProductoList (ListView):                    
    model = Producto
    template_name = 'Juguetes/producto_list.html'
 
class ProductoCreate (CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Juguetes/producto_form.html'
    success_url = reverse_lazy('producto_list')
 
class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Juguetes/producto_form.html'
    success_url = reverse_lazy('producto_list')
 
class ProductoDelete(DeleteView):
    model = ProductoForm
    template_name = 'Juguetes/producto_borrar.html'
    success_url = reverse_lazy('producto_list')
 

