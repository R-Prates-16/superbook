from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import VillainForm
from .models import Villain

def lista_viloes(request):
    viloes = Villain.objects.all()
    return render(request, "villains/lista_viloes.html", {"viloes": viloes})

def criar_vilao(request):
    if request.method == "POST":
        form = VillainForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vilão criado com sucesso!')
            return redirect('lista_viloes')
    else:
        form = VillainForm()
    return render(request, "villains/form_vilao.html", {"form": form})

def detalhe_vilao(request, pk):
    vilao = get_object_or_404(Villain, pk=pk)
    return render(request, "villains/detalhe_vilao.html", {"vilao": vilao})

def editar_vilao(request, pk):
    vilao = get_object_or_404(Villain, pk=pk)
    if request.method == "POST":
        form = VillainForm(request.POST, request.FILES, instance=vilao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vilão atualizado com sucesso!')
            return redirect('lista_viloes')
    else:
        form = VillainForm(instance=vilao)
    return render(request, "villains/form_vilao.html", {"form": form})

def excluir_vilao(request, pk):
    vilao = get_object_or_404(Villain, pk=pk)
    if request.method == "POST":
        vilao.delete()
        messages.success(request, 'Vilão excluído com sucesso!')
        return redirect('lista_viloes')
    return render(request, "villains/excluir_vilao.html", {"vilao": vilao})