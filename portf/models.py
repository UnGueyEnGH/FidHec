from django.db import models


class RegistroPrueba(models.Model):
    """
    Modelo multipropósito para experimentar con diferentes tipos de datos 
    y probar la lógica del CRUD desde views.py y forms.py.
    """
    
    NIVELES = [
        ('BAS', 'Básico'),
        ('INT', 'Intermedio'),
        ('ADV', 'Avanzado'),
    ]

    nombre = models.CharField(
        max_length=80, 
        verbose_name="Nombre del Elemento"
    )

    descripcion = models.TextField(
        blank=True, 
        verbose_name="Descripción Corta"
    )

    prioridad = models.IntegerField(
        default=1, 
        verbose_name="Prioridad (Número)"
    )

    costo_estimado = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        default=0.00, 
        verbose_name="Costo / Valor Decimal"
    )

    nivel_dificultad = models.CharField(
        max_length=3, 
        choices=NIVELES, 
        default='BAS', 
        verbose_name="Nivel de Dificultad"
    )

    completado = models.BooleanField(
        default=False, 
        verbose_name="¿Completado?"
    )

    fecha_entrega = models.DateField(
        null=True, 
        blank=True, 
        verbose_name="Fecha de Entrega"
    )

    creado_el = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Fecha de Registro"
    )

    class Meta:
        verbose_name = "Registro de Prueba"
        verbose_name_plural = "Registros de Prueba"
        ordering = ['-creado_el']

    def __str__(self):
        estado = "✅" if self.completado else "⏳"
        return f"{estado} {self.nombre} | {self.get_nivel_dificultad_display()} (${self.costo_estimado})"