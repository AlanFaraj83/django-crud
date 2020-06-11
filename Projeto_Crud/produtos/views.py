from django.shortcuts import render
from .models import Produto

def home(request):
    nome = 'Samsung'
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def produto(request, codigo):
    produto = Produto.objects.get(id=codigo)
    return render(request, 'produtos.html', {'produto': produto})



