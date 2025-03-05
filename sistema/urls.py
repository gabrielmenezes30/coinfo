from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Importa todas as views corretamente

urlpatterns = [
    # Página inicial
    path('', views.home, name="home"),

    # Notícias
    path('noticias/', views.lista_noticias, name='lista_noticias'),
    path('noticia/<int:pk>/', views.detalhe_noticia, name='detalhe_noticia'),
    path('noticias/cadastrar/', views.cadastrar_noticia, name='cadastrar_noticia'),

    # Login e Logout
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'), 

    path('perfil/', views.perfil_usuario, name='perfil_usuario'),

    # Cursos
    path('cursos/', views.cursos_list, name='listar_cursos'),
    path('cursos/criar/', views.cadastrar_curso, name='criar_curso'),

    # Projetos
    path('projetos/', views.projetos_list, name='listar_projetos'),
    path('projetos/criar/', views.cadastrar_projeto, name='criar_projeto'),

    # Infraestrutura
    path('infraestrutura/', views.infraestrutura_list, name='listar_infraestrutura'),
    path('infraestrutura/criar/', views.cadastrar_infraestrutura, name='criar_infraestrutura'),
]
