# Generated by Django 5.1.6 on 2025-03-04 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('modalidade', models.CharField(default='Superior', max_length=50)),
                ('link_atas_nde', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Infraestrutura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='infraestrutura/')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('link_lattes', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('link', models.URLField(blank=True, null=True)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='projetos/')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projetos', to='sistema.professor')),
            ],
        ),
    ]
