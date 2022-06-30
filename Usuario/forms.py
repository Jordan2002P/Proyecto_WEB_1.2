from django import forms
from .models import Usuario
 
class RegistroForm(forms.ModelForm):
 
    class Meta:
        model = Usuario
        fields = [
                'username',
                'nombre',
                'email',
                'password',
            ]
        labels = {
                'username': 'Nombre de usuario',
                'nombre': 'Nombre',
                'email': 'Correo',
                'password': 'Contraseña',
        }
