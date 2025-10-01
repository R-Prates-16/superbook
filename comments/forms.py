from django import forms
from .models import Comentario

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["conteudo"]  # Removemos 'autor' pois será preenchido automaticamente
        widgets = {
            'conteudo': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Deixe seu comentário...',
                'class': 'form-control'
            }),
        }
        labels = {
            'conteudo': ''
        }


# Rian Prates