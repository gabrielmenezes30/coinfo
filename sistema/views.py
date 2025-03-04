from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from .forms import NoticiaForm, CursoForm, ProjetoForm, InfraestruturaForm
from .models import Noticia, Curso, Projeto, Infraestrutura
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate
from .forms import RegistroForm


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redireciona para a home após o registro
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

# Verifica se o usuário é admin
def is_admin(user):
    return user.is_staff or user.is_superuser

# Verifica se o usuário é professor
def is_professor(user):
    return user.groups.filter(name='Professores').exists()

# 📌 CADASTRAR NOTÍCIA
@login_required
@user_passes_test(is_admin)
def cadastrar_noticia(request):
    if request.method == "POST":
        form = NoticiaForm(request.POST)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.save()
            return redirect('home')
    else:
        form = NoticiaForm()
    
    return render(request, 'noticias/cadastrar.html', {'form': form})

def lista_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/lista.html', {'noticias': noticias})

# 📌 DETALHAR NOTÍCIA
def detalhe_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'noticias/detalhe.html', {'noticia': noticia})


# 📌 HOME (EXIBE AS 3 ÚLTIMAS NOTÍCIAS)
def home(request):

    is_admin = request.user.is_superuser
    is_professor = request.user.groups.filter(name='Professores').exists()
    noticias = Noticia.objects.filter(status='publicado', ativacao='ativada').order_by('-data_publicacao')[:3]

    return render(request, 'index.html', {
        'noticias': noticias,
        'is_admin': is_admin,
        'is_professor': is_professor,
        })

# 📌 LISTAR CURSOS
def cursos_list(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista.html', {'cursos': cursos})

# 📌 CADASTRAR CURSO (Apenas Admins)
@login_required
@user_passes_test(is_admin)
def cadastrar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    
    return render(request, 'cursos/cadastrar.html', {'form': form})

# 📌 LISTAR PROJETOS
def projetos_list(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos/lista.html', {'projetos': projetos})

# 📌 CADASTRAR PROJETO (Apenas Professores)
@login_required
@user_passes_test(is_admin)
@user_passes_test(lambda u: u.groups.filter(name='Professores').exists())  # Garantir que o usuário é professor
def cadastrar_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.professor = request.user  # Define o professor como o usuário logado
            projeto.save()
            return redirect('listar_projetos')
    else:
        form = ProjetoForm()

    return render(request, 'projetos/cadastrar.html', {
        'form': form,
        'is_admin': is_admin,
        'is_professor': is_professor,
    })

# 📌 LISTAR INFRAESTRUTURA
def infraestrutura_list(request):
    infraestrutura = Infraestrutura.objects.all()
    return render(request, 'infraestrutura/lista.html', {'infraestrutura': infraestrutura})

# 📌 CADASTRAR INFRAESTRUTURA (Apenas Admins)
@login_required
@user_passes_test(is_admin)
def cadastrar_infraestrutura(request):
    if request.method == "POST":
        form = InfraestruturaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('infraestrutura_list')
    else:
        form = InfraestruturaForm()
    
    return render(request, 'infraestrutura/cadastrar.html', {'form': form})
