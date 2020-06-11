from django.shortcuts import render
from .models import Fornecedor

def home1(request):
    nome = 'Microsoft'
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores.html', {'fornecedores': fornecedores})

def fornecedor(request, codigo):
    fornecedor= fornecedor.objects.get(id=codigo)
    return render(request, 'fornecedores.html', {'fornecedor': fornecedor})
