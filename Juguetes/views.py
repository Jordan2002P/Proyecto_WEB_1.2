

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
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductoSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status


class API_objects(generics.ListCreateAPIView): 
    queryset = Producto.objects.all() 
    serializer_class = ProductoSerializer 


class API_objects_details(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Producto.objects.all() 
    serializer_class = ProductoSerializer 

@api_view(['GET', 'POST'])
def producto_collection(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def producto_element(request, pk):
    producto = get_object_or_404(Producto, id=pk)

    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
 
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
 

