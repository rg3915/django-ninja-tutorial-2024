from django.contrib import admin

from .models import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'idade', 'ativo')
    readonly_fields = (
        'slug',
        'criado_em',
        'modificado_em',
        'criado_por',
        'modificado_por',
    )
    search_fields = ('nome',)
    list_filter = ('ativo',)
