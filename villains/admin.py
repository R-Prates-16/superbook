from django.contrib import admin
from .models import Villain

@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    list_display = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'nivel_ameaca', 'criado_em']
    list_filter = ['cidade', 'nivel_ameaca']
    search_fields = ['codinome', 'nome_real', 'cidade']

    fieldsets = (
        ('Identidade', {
            'fields': ('codinome', 'nome_real')
        }),
        ('Informações', {
            'fields': ('poder_principal', 'cidade', 'nivel_ameaca', 'historia', 'imagem')
        }),
        ('Registro', {
            'fields': ('criado_em',)
        }),
    )

    readonly_fields = ['criado_em']
# Rian Prates