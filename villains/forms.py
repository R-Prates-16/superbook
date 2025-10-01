from django import forms
from .models import Villain

class VillainForm(forms.ModelForm):
    class Meta:
        model = Villain
        fields = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'nivel_ameaca', 'historia', 'imagem']
        widgets = {
            'historia': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Conte a história do vilão...',
                'class': 'form-control'
            }),
            'codinome': forms.TextInput(attrs={
                'placeholder': 'Ex: Coringa, Duas-Caras',
                'class': 'form-control'
            }),
            'poder_principal': forms.TextInput(attrs={
                'placeholder': 'Ex: Manipulação mental, Tecnologia avançada',
                'class': 'form-control'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'nivel_ameaca': forms.Select(attrs={
                'class': 'form-control'
            }),
            'imagem': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }
        labels = {
            'nome_real': 'Nome Real',
            'nivel_ameaca': 'Nível de Ameaça',
            'imagem': 'Foto do Vilão'
        }

# Rian Prates