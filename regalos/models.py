from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Persona(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='persona', null=True, blank=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
    
    def total_regalos(self):
        return self.regalos.count()
    
    def total_gastado(self):
        return sum(regalo.precio for regalo in self.regalos.all())
    
    def puede_agregar_regalo(self):
        return self.regalos.count() < 6
    
    def tiene_lista_completa(self):
        return self.regalos.count() == 6
    
    def regalos_faltantes(self):
        return 6 - self.regalos.count()

class Regalo(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='regalos')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        validators=[
            MinValueValidator(0.01),
            MaxValueValidator(25.00)
        ]
    )
    comprado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Regalo'
        verbose_name_plural = 'Regalos'
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.nombre} - S/ {self.precio}"
    
    def clean(self):
        if self.precio and self.precio > 25:
            raise ValidationError('El precio no puede ser mayor a S/ 25.00')
        
        if self.persona_id:
            regalos_count = Regalo.objects.filter(persona=self.persona).exclude(pk=self.pk).count()
            if regalos_count >= 6:
                raise ValidationError('Esta persona ya tiene el máximo de 6 regalos')
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
