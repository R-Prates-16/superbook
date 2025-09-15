from django.db import models
from posts.models import Post
from heroes.models import Hero

class Comentario(models.Model):
    autor = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="comments")
    conteudo = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)