from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from comments.forms import CommentForm
from comments.models import Comentario

class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_posts')

def detalhes_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    comentarios = Comentario.objects.filter(post=post)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("detalhes_post", pk=post.pk)
    else:
        form = CommentForm()

    return render(request, "posts/detail_post.html", {"post": post, "form": form, "comentarios": comentarios})



#Rian Prates