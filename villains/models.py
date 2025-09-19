from django.db import models

class Villain(models.Model):
    NIVEL_AMECACA_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
        ('critica', 'Crítica')
    ]
    
    codinome = models.CharField(max_length=100)
    nome_real = models.CharField(max_length=100, blank=True, null=True)
    poder_principal = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    nivel_ameaca = models.CharField(max_length=20, choices=NIVEL_AMECACA_CHOICES, default='media')
    historia = models.TextField()
    imagem = models.ImageField(upload_to='fotos_viloes/', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Villain'
        verbose_name_plural = 'Villains'

    def __str__(self):
        return self.codinome