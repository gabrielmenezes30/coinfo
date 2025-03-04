from django import forms
from .models import Noticia
from django_summernote.widgets import SummernoteWidget

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'conteudo', 'status', 'ativacao']
        widgets = {
            'conteudo': SummernoteWidget(),  # Aplica o editor Summernote ao campo 'conteudo'
        }
        