from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import HeroForm
from .models import Hero

def criar_heroi(request):
    if request.method == "POST":
        form = HeroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Herói criado com sucesso!')
            return redirect('lista_herois')
    else:
        form = HeroForm()
    return render(request, "heroes/form_heroi.html", {"form": form})

def lista_herois(request):
    herois = Hero.objects.all()
    return render(request, "heroes/lista_herois.html", {"herois": herois})

def detalhe_heroi(request, pk):
    heroi = get_object_or_404(Hero, pk=pk)
    return render(request, "heroes/detalhe_heroi.html", {"heroi": heroi})

def editar_heroi(request, pk):
    heroi = get_object_or_404(Hero, pk=pk)
    if request.method == "POST":
        form = HeroForm(request.POST, request.FILES, instance=heroi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Herói atualizado com sucesso!')
            return redirect('lista_herois')
    else:
        form = HeroForm(instance=heroi)
    return render(request, "heroes/form_heroi.html", {"form": form})

def excluir_heroi(request, pk):
    heroi = get_object_or_404(Hero, pk=pk)
    if request.method == "POST":
        heroi.delete()
        messages.success(request, 'Herói excluído com sucesso!')
        return redirect('lista_herois')
    return render(request, "heroes/excluir_heroi.html", {"heroi": heroi})
# Rian Prates