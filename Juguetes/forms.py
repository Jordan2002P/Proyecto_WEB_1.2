from .models import Producto
from django import forms

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = (
            'fotografia',
            'codigo',
            'nombre',
            'tipo_juguete'
        )
        labels = {
            'fotografia':'Fotografia',
            'codigo':'Codigo',
            'nombre':'Nombre',
            'tipo_juguete':'Tipo Juguete'
        }
        widgets = {
            'codigo':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_juguete':forms.Select(choices="JUGUETES_MASCOTAS", attrs={'class':'form-control'})
        }