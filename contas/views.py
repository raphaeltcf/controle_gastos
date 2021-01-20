from django.shortcuts import render, redirect
from .models import transacoes
import datetime
from .forms import transacaoform

def home(request):
    data = {}

    data['now'] = datetime.datetime.now()
    return render(request, "contas/home.html", data)

def listagem(request):
    data = {}
    data["transacao"] = transacoes.objects.all() 
    return render(request, 'contas/listagem.html', data)
    
    
def nova_transacao(request):
    data = {}
    form = transacaoform(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'contas/form.html', data)

def update(request, pk):
    data = {}
    transacao = transacoes.objects.get(pk=pk)
    form = transacaoform(request.POST or None, instance=transacao)


    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = transacoes.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')

