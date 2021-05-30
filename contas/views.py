from django.shortcuts import render, redirect
from .models import Transacao
from .forms import TransacaoForm

def home(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/home.html', data)

def novaTransacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    
    data['form'] = form  
    return render(request, 'contas/form.html', data)

def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('home')
    
    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
   
    return redirect('home')