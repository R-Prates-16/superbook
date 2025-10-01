from django.db import models
from heroes.models import Hero

class Post(models.Model):
    autor = models.ForeignKey(Hero, on_delete=models.CASCADE)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Post de {self.autor.codinome}"