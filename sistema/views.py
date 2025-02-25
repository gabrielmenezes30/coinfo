from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def professores_list(request):
    return render(request, 'professores/professores.html')