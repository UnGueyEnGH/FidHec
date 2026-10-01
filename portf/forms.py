from django import forms
from .models import RegistroPrueba


class RegistroPruebaForm(forms.ModelForm):

    class Meta:
        model = RegistroPrueba
        fields = [
            'nombre',
            'descripcion',
            'prioridad',
            'costo_estimado',
            'nivel_dificultad',
            'completado',
            'fecha_entrega',
        ]
        
        # Personalización de etiquetas visibles en el formulario
        labels = {
            'nombre': 'Nombre del Registro',
            'descripcion': 'Descripción',
            'prioridad': 'Prioridad (1-10)',
            'costo_estimado': 'Costo/Valor ($)',
            'nivel_dificultad': 'Nivel de Dificultad',
            'completado': '¿Marcar como Completado?',
            'fecha_entrega': 'Fecha de Entrega',
        }

        # Widgets con asignación limpia de clases CSS para el stylesheet externo
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Prueba de módulo ORM',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Escribe detalles del registro...',
            }),
            'prioridad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 10,
            }),
            'costo_estimado': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00',
            }),
            'nivel_dificultad': forms.Select(attrs={
                'class': 'form-control',
            }),
            'completado': forms.CheckboxInput(attrs={
                'class': 'form-checkbox-input',
            }),
            'fecha_entrega': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }