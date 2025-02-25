from django.urls import path
from .views import home, professores_list, cursos

urlpatterns = [
    path('', home, name="home"),
    path('professores/', professores_list, name="professores_list"),
    path('cursos/', cursos, name="cursos"),
]
