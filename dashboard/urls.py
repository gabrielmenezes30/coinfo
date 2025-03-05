from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('dashboard/atribuir_professor/<int:user_id>/', views.atribuir_professor, name='atribuir_professor'),
    path('remover_professor/<int:user_id>/', views.remover_professor, name='remover_professor'),

    path('noticias_desativadas', views.noticias_desativadas, name="noticias_desativadas")
]
