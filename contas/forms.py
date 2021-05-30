from django.forms import ModelForm
from .models import Categoria, Transacao

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']