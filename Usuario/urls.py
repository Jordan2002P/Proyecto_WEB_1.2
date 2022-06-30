from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList

urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('listar', UserList.as_view(), name="usuario_list"),
    path('edit_usuario/<int:pk>', views.UserUpdate.as_view(), name='edit_usuario'),
    path('del_usuario/<int:pk>', views.UserDelete.as_view(), name='del_usuario'),
]
