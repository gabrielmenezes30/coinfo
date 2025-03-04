from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Noticia, Infraestrutura, Curso, Projeto

# Configuração para Notícia
class NoticiaAdmin(SummernoteModelAdmin):
    summernote_fields = ('conteudo',)

# Registro de outras models
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Infraestrutura)
admin.site.register(Curso)
admin.site.register(Projeto)
