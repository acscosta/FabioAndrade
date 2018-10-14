from django.contrib import admin
from .models import Aluno, Mensalidade, Conta

# Register your models here.

admin.site.register(Aluno)
admin.site.register(Mensalidade)
admin.site.register(Conta)