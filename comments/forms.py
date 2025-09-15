from django import forms
from .models import Comentario

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["autor", "conteudo"]
        widgets = {
            'autor': forms.Select(attrs={'class': 'form-control'})
        }