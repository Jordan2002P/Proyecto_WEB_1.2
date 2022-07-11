from django.urls import path
# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductoList, ProductoCreate, ProductoUpdate , ProductoDelete
from django.contrib.auth.views import login_required
 
urlpatterns = [
    path('listar/', login_required(ProductoList.as_view), name="producto_list"),
 
    path('crear/', login_required(ProductoCreate.as_view), name="producto_form"),
    path('editar/<int:pk>', login_required(ProductoUpdate.as_view), name="producto_update"),
    path('borrar/<int:pk>',  login_required(ProductoDelete.as_view), name="producto_borrar"),
    
    
    
]

from rest_framework.urlpatterns import format_suffix_patterns 

from Juguetes import views 



urlpatterns = [ 
    path('api/', views.API_objects.as_view()), 
    path('api/<int:pk>/', views.API_objects_details.as_view()), 
] 



urlpatterns = format_suffix_patterns(urlpatterns) 
