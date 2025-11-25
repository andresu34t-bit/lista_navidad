from django import forms
from .models import Persona, Regalo

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email (opcional)'}),
        }

class RegaloForm(forms.ModelForm):
    class Meta:
        model = Regalo
        fields = ['nombre', 'descripcion', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del regalo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción (opcional)'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio (máx. S/ 25.00)', 'step': '0.01', 'max': '25.00'}),
        }
