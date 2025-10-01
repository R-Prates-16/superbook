from django import forms
from .models import Post
from heroes.models import Hero  # ← Importar o modelo Hero

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['autor', 'mensagem']  # ← Adicionar 'autor' nos fields
        widgets = {
            'mensagem': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'O que está acontecendo no mundo dos super-heróis?',
                'class': 'form-control'
            }),
            'autor': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'mensagem': 'Mensagem',
            'autor': 'Herói'
        }
# Rian Prates