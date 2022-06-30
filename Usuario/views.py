from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegistroForm
from .models import Usuario
from django.shortcuts import render, redirect



class RegistroUsuario(CreateView):
    model = Usuario
    template_name = "Usuario/usuario_form.html"
    form_class = RegistroForm
    success_url = reverse_lazy('usuario_list')
 
 
class UserList(ListView):
    model = Usuario
    template_name = 'Usuario/usuario_list.html'

class UserUpdate(UpdateView):
    model = Usuario
    form_class = RegistroForm
    template_name = 'Usuario/usuario_form.html'
    success_url = reverse_lazy('usuario_list')

class UserDelete(DeleteView):
    model = Usuario
    template_name = 'Usuario/usuario_delete.html'
    success_url = reverse_lazy('usuario_list')


def borrar_usuario(request, usuario_id):
    instancia = Usuario.objects.get(id=usuario_id)
    instancia.delete()
    return redirect('usuario_list')

def edit_usuario(request, usuario_id):
    instancia = Usuario.objects.get(id=usuario_id)
    form = RegistroForm(instance=instancia)
    if request.method == "POST":
        form = RegistroForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request, "Usuario/edit_usuario.html", {'form': form})