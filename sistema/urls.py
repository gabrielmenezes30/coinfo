from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, professores_list, cursos, cadastrar_noticia, lista_noticias, detalhe_noticia

urlpatterns = [
    path('', home, name="home"),
    path('professores/', professores_list, name="professores_list"),
    path('cursos/', cursos, name="cursos"),

    # Notícias
    path('noticias/', lista_noticias, name='lista_noticias'),
    path('noticia/<int:pk>/', detalhe_noticia, name='detalhe_noticia'),
    path('noticias/cadastrar/', cadastrar_noticia, name='cadastrar_noticia'),

    # Login e Logout
    # Login e Logout
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
