from django import forms
from .models import Noticia, Curso, Projeto, Infraestrutura
from django.contrib.auth.forms import UserCreationForm
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
        fields = ['titulo', 'link', 'descricao', 'imagem']

# 📌 Formulário para Infraestrutura
class InfraestruturaForm(forms.ModelForm):
    class Meta:
        model = Infraestrutura
        fields = ['titulo', 'descricao', 'imagem']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # Desabilitando mensagens de ajuda e adicionando classes Bootstrap
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None
            field.widget.attrs.update({'class': 'form-control'})

    # Validando se o nome de usuário é único
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso.')
        return username

    # Validando se o email é único
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está em uso.')
        return email

    # Validando se as senhas são iguais
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('As senhas não coincidem.')
        return password2

    # Validando a força da senha
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError('A senha deve ter pelo menos 8 caracteres.')
        if password1.isnumeric():
            raise forms.ValidationError('A senha não pode ser completamente numérica.')
        if password1.lower() == password1:
            raise forms.ValidationError('A senha deve conter pelo menos uma letra maiúscula.')
        if password1.lower() == password1:
            raise forms.ValidationError('A senha deve conter pelo menos uma letra minúscula.')
        return password1