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


# 🏫 Curso
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    modalidade = models.CharField(max_length=50, default="Superior")
    link_atas_nde = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome


# 📚 Projeto
class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    link = models.URLField(blank=True, null=True)
    descricao = models.TextField()
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projetos")
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)

    def __str__(self):
        return self.titulo


# 🏢 Infraestrutura
class Infraestrutura(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='infraestrutura/', blank=True, null=True)

    def __str__(self):
        return self.titulo
