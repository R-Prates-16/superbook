from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from comments.models import Comentario
from comments.forms import CommentForm
from heroes.models import Hero  

class PostListView(ListView):
    model = Post
    template_name = 'posts/lista_posts.html'
    context_object_name = 'posts'
    ordering = ['-criado_em']

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/novo_post.html'
    success_url = reverse_lazy('lista_posts')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrar apenas heróis disponíveis
        form.fields['autor'].queryset = Hero.objects.all().order_by('codinome')
        return form
    
    def form_valid(self, form):
        messages.success(self.request, 'Post criado com sucesso!')
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/editar_post.html'
    success_url = reverse_lazy('lista_posts')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['autor'].queryset = Hero.objects.all().order_by('codinome')
        return form
    
    def form_valid(self, form):
        messages.success(self.request, 'Post atualizado com sucesso!')
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/excluir_post.html'
    success_url = reverse_lazy('lista_posts')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Post excluído com sucesso!')
        return super().delete(request, *args, **kwargs)

# Function-Based View para detalhes com comentários
def detalhe_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.all()
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            # Solução temporária: usar o primeiro herói disponível
            from heroes.models import Hero
            comentario.autor = Hero.objects.first()
            comentario.save()
            messages.success(request, 'Comentário adicionado!')
            return redirect('detalhe_post', pk=post.pk)
    else:
        form = CommentForm()
    
    return render(request, 'posts/detalhe_post.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form
    })