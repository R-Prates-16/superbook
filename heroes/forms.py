from django import forms
from .models import Hero

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'email_contato', 'historia', 'imagem']
        widgets = {
            'historia': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Conte a história do herói...',
                'class': 'form-control'
            }),
            'codinome': forms.TextInput(attrs={
                'placeholder': 'Ex: Superman, Batman',
                'class': 'form-control'
            }),
            'poder_principal': forms.TextInput(attrs={
                'placeholder': 'Ex: Super força, Voo',
                'class': 'form-control'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email_contato': forms.EmailInput(attrs={
                'placeholder': 'exemplo@email.com',
                'class': 'form-control'
            }),
            'imagem': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }
        labels = {
            'email_contato': 'Email de Contato',
            'nome_real': 'Nome Real',
            'imagem': 'Foto do Herói'
        }
# Rian Prates