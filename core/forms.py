from django.forms import ModelForm
from .models import Aluno, Mensalidade


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'


class MensalidadeForm(ModelForm):
    class Meta:
        model = Mensalidade
        fields = '__all__'
