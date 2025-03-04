from django.contrib import admin
from .models import Noticia
from django_summernote.admin import SummernoteModelAdmin

class NoticiaAdmin(SummernoteModelAdmin):
    summernote_fields = ('conteudo',)

admin.site.register(Noticia, NoticiaAdmin)