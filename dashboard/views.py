from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group, Permission
from sistema.models import Noticia

# Função para verificar se o usuário é admin
def is_admin(user):
    return user.is_authenticated and user.is_staff


@login_required
@user_passes_test(is_admin)
def index(request):
    query = request.GET.get('q', '')  
    usuarios = User.objects.filter(username__icontains=query) if query else []  

    is_admin = request.user.is_staff and not request.user.groups.filter(name='Professores').exists()
    is_professor = request.user.groups.filter(name='Professores').exists()

    # Filtrando notícias desativadas e em rascunho
    noticias_desativadas = Noticia.objects.filter(ativacao='desativada').order_by('-data_publicacao')
    noticias_rascunho = Noticia.objects.filter(status='rascunho').order_by('-data_publicacao')

    return render(request, 'dashboard/index.html', {
        'usuarios': usuarios,   
        'is_admin': is_admin,
        'is_professor': is_professor,
        'query': query,
        'noticias_desativadas': noticias_desativadas,
        'noticias_rascunho': noticias_rascunho
    })


@login_required
@user_passes_test(is_admin)
def atribuir_professor(request, user_id):
    user = User.objects.get(id=user_id)

    # Adicionar usuário ao grupo "Professores"
    grupo, created = Group.objects.get_or_create(name='Professores')
    user.groups.add(grupo)

    # Tornar usuário staff (mas não superusuário)
    user.is_staff = True
    user.save()

    # Definir permissões específicas (exemplo: pode visualizar e editar usuários)
    permissoes = Permission.objects.filter(codename__in=[
        'view_user', 'change_user',  # Permissões específicas de usuário
        'add_course', 'change_course', 'view_course',  # Exemplo: permissões para cursos
    ])
    user.user_permissions.add(*permissoes)

    return redirect('dashboard')


@login_required
@user_passes_test(is_admin)
def remover_professor(request, user_id):
    user = User.objects.get(id=user_id)

    # Remover do grupo "Professores"
    grupo = Group.objects.filter(name='Professores').first()
    if grupo:
        user.groups.remove(grupo)

    # Remover status de staff
    user.is_staff = False
    user.save()

    # Remover permissões concedidas
    permissoes = Permission.objects.filter(codename__in=[
        'view_user', 'change_user',  
        'add_course', 'change_course', 'view_course',  
    ])
    user.user_permissions.remove(*permissoes)

    return redirect('dashboard')

def noticias_desativadas(request):
    noticias_desativadas = Noticia.objects.filter(ativacao='desativada').order_by('-data_publicacao')
    is_admin = request.user.is_staff and not request.user.groups.filter(name='Professores').exists()
    return render(request, 'dashboard/noticias_desativadas.html', {
        'noticias_desativadas':noticias_desativadas,
        'is_admin':is_admin,
    })

