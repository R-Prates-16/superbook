from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Comentario
from .forms import CommentForm

@login_required
def criar_comentario(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user.hero
            comentario.post_id = post_id
            comentario.save()
            messages.success(request, 'Comentário adicionado!')
            return redirect('detalhe_post', pk=post_id)
    return redirect('detalhe_post', pk=post_id)

class EditarComentarioView(LoginRequiredMixin, UpdateView):
    model = Comentario
    form_class = CommentForm
    template_name = 'comments/editar_comentario.html'
    
    def get_success_url(self):
        return reverse_lazy('detalhe_post', kwargs={'pk': self.object.post.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Comentário atualizado com sucesso!')
        return super().form_valid(form)

class ExcluirComentarioView(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'comments/excluir_comentario.html'
    
    def get_success_url(self):
        return reverse_lazy('detalhe_post', kwargs={'pk': self.object.post.pk})
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Comentário excluído com sucesso!')
        return super().delete(request, *args, **kwargs)