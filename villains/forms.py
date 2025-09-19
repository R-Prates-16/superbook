from django import forms
from .models import Villain

class VillainForm(forms.ModelForm):
    class Meta:
        model = Villain
        fields = ['codinome', 'nome_real', 'poder_principal', 'cidade', 
                 'nivel_ameaca', 'historia', 'imagem']
        widgets = {
            'historia': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Conte a história do vilão...'}),
            'codinome': forms.TextInput(attrs={'placeholder': 'Ex: Coringa, Duas-Caras'}),
            'poder_principal': forms.TextInput(attrs={'placeholder': 'Ex: Manipulação mental, Tecnologia avançada'}),
        }
        labels = {
            'nivel_ameaca': 'Nível de Ameaça'
        }