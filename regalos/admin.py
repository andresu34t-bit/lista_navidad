from django.contrib import admin
from .models import Persona, Regalo

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'total_regalos', 'total_gastado', 'fecha_creacion']
    search_fields = ['nombre', 'email']
    
@admin.register(Regalo)
class RegaloAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'persona', 'precio', 'comprado', 'fecha_creacion']
    list_filter = ['comprado', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion', 'persona__nombre']
    list_editable = ['comprado']
