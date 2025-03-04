from django import forms
from .models import Noticia, Curso, Projeto, Infraestrutura
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.models import User

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'conteudo', 'status', 'ativacao']
        widgets = {
            'conteudo': SummernoteWidget(),  # Aplica o editor Summernote ao campo 'conteudo'
        }

# 📌 Formulário para Curso
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'modalidade', 'link_atas_nde']

# 📌 Formulário para Projeto
class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'link', 'descricao', 'professor', 'imagem']

# 📌 Formulário para Infraestrutura
class InfraestruturaForm(forms.ModelForm):
    class Meta:
        model = Infraestrutura
        fields = ['titulo', 'descricao', 'imagem']