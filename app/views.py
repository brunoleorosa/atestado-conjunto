from django.shortcuts import render, redirect
from app.forms import *
from app.models import Atestados
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    data = {}
    data['db'] = Atestados.objects.all()
    return render(request, 'index.html', data)

#pesquisa = referente à página de pesquisa
def pesquisa(request):
    data = {}
    atestados = list(Atestados.objects.all())
    lista = []
    if request.method == "GET":
        numero = request.GET.get('numero_documento', default=None)
        for num in numero:
            num = numero.numero_documento
        servico = request.GET.getlist('tipo_servico', default=None)
        data_emissao = request.GET.getlist('data_emissao', default=None)
        cliente = request.GET.getlist('cliente_id', default=None)
        empresa = request.GET.getlist('empresa_id', default=None)

        for atest in atestados:
            if atest.numero_documento == num:
                lista.append(atest)
                data['atestados'] = lista
        else:
            data['dados'] = Atestados.objects.all()
        return render(request, 'pesquisa.html', data)

def form(request):
    data = {}
    data['form'] = AtestadosForm()
    return render(request, 'atestado_form.html', data)

# Função para cadastrar atestados
def create(request):
    form = AtestadosForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')

# Função para visualizar detalhes de atestados cadastrados
def view(request, pk):
    data = {}
    data['db'] = Atestados.objects.get(pk=pk)
    return render(request, 'view.html', data)

#search = método que pega o conteúdo de um formulário
def search(request):
    return None

#searchall = pesquisa todos os campos
def searchall(request):
    dados = {}
    dados['db'] = Atestados.objects.all()
    return render(request, 'pesquisa.html', dados)

# Função para tela de edição de atestados
def edit(request, pk):
    data = {}
    data['db'] = Atestados.objects.get(pk=pk)
    data['form'] = AtestadosForm(instance=data['db'])
    return render(request, 'atestado_form.html', data)

# Função para atualizar edições de atestados
def update(request, pk):
    data = {}
    data['db'] = Atestados.objects.get(pk=pk)
    form = AtestadosForm(request.POST, request.FILES or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

# Função para deletar atestados
def delete(request, pk):
    db = Atestados.objects.get(pk=pk)
    db.delete()
    return redirect('pesquisa')
