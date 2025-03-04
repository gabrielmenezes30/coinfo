from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import NoticiaForm
from .models import Noticia

def is_admin(user):
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(is_admin)
def cadastrar_noticia(request):
    if request.method == "POST":
        form = NoticiaForm(request.POST)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user  # Define o usuário logado como autor
            noticia.save()
            return redirect('home')  # Redireciona para a lista de notícias
    else:
        form = NoticiaForm()
    
    return render(request, 'noticias/cadastrar.html', {'form': form})

# View para listar notícias
def lista_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/lista.html', {'noticias': noticias})

# View para detalhes de uma notícia específica
def detalhe_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'noticias/detalhe.html', {'noticia': noticia})

def home(request):
    noticias = Noticia.objects.filter(status='publicado', ativacao='ativada').order_by('-data_publicacao')[:3]
    return render(request, 'index.html', {'noticias': noticias})



def professores_list(request):
    return render(request, 'professores/professores.html')

def cursos(request):
    return render(request, 'cursos.html')
