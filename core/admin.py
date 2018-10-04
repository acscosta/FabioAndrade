from django.contrib import admin
from .models import Aluno, Mensalidade

# Register your models here.

admin.site.register(Aluno)
admin.site.register(Mensalidade)