from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def servicios(request):
    return render(request, 'app/servicios.html')

def accesorios(request):
    return render(request, 'app/accesorios.html')

def guarderia(request):
    return render(request, 'app/guarderia.html')

def comida(request):
    return render(request, 'app/comida.html')

def adoptados(request):
    return render(request, 'app/adoptados.html')

def peluqueria(request):
    return render(request, 'app/peluqueria.html')