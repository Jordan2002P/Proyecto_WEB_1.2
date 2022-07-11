from django.urls import path
from .views import home, accesorios, servicios, guarderia, comida, adoptados, peluqueria

urlpatterns = [
    path('', home, name="home"),
    path('servicios/', servicios, name="servicios"),
    path('accesorios/', accesorios, name="accesorios"),
    path('guarderia/', guarderia, name="guarderia"),
    path('comida/', comida, name="comida"),
    path('adoptados/', adoptados, name="adoptados"),
    path('peluqueria/', peluqueria, name="peluqueria"),
]


