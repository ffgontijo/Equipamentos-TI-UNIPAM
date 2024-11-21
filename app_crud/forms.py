from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'descricao', 'numero_patrimonio', 'data_aquisicao', 'status']
        widgets = {
            'data_aquisicao': forms.DateInput(attrs={'type': 'date'}),
        }
