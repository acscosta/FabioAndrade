from django.forms import ModelForm
from .models import Aluno, Mensalidade, Conta


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'


class MensalidadeForm(ModelForm):
    class Meta:
        model = Mensalidade
        fields = '__all__'


class ContaForm(ModelForm):
    class Meta:
        model = Conta
        fields = '__all__'
