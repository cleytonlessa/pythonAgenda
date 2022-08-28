from django.contrib import admin
from . models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone',
                    'email', 'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    # list_filter = ('id', 'nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('id', 'nome', 'sobrenome', 'telefone',
                     'email', 'data_criacao', 'categoria', 'mostrar')
    list_editable = ('telefone', 'mostrar')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
