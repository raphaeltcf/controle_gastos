from django.forms import ModelForm
from .models import transacoes

class transacaoform(ModelForm):
    class Meta:
        model = transacoes
        fields = ['data', 'valor', 'categoria', 'observacoes', 'descricao']