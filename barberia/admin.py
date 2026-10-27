from django.contrib import admin
from .models import Cliente, Barbero

@admin.register(Barbero)
class BarberoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'especialidad')
    search_fields = ('nombre',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Columnas que se mostrarán en la tabla principal del admin
    list_display = ('nombre', 'apellido', 'telefono', 'barbero_asignado', 'proxima_cita')
    # Filtros laterales rápidos para buscar por barbero o fechas de citas
    list_filter = ('barbero_asignado', 'proxima_cita')
    # Buscador avanzado
    search_fields = ('nombre', 'apellido', 'telefono')
