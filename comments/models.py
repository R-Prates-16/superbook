from django.db import models
from posts.models import Post
from heroes.models import Hero

class Comentario(models.Model):
    autor = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="comentarios")
    conteudo = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['criado_em']
    
    def __str__(self):
        return f"Comentário de {self.autor.codinome} em {self.post}"