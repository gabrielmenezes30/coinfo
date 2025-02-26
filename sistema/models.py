from django.db import models
from django.contrib.auth.models import User

class Noticia(models.Model):
    STATUS_CHOICES = [
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    ]
    
    ATIVACAO_CHOICES = [
        ('ativada', 'Ativada'),
        ('desativada', 'Desativada'),
    ]

    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='rascunho')
    ativacao = models.CharField(max_length=10, choices=ATIVACAO_CHOICES, default='ativada')


    def __str__(self):
        return self.titulo
