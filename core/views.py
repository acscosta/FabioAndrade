from django.shortcuts import render, redirect
from .models import Aluno, Mensalidade
from .forms import (AlunoForm, MensalidadeForm)
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {'mensagem': 'Gesielle Te amo!'}
    return render(request, 'core/index.html', context)

@login_required
def lista_alunos(request):
    alunos = Aluno.objects.all()
    form = AlunoForm()
    data = {'alunos': alunos, 'form':form}
    return render(request, 'core/lista_alunos.html', data)

@login_required
def lista_mensalidades(request):
    mensalidades = Mensalidade.objects.all()
    form = MensalidadeForm()
    data = {'mensalidades': mensalidades, 'form':form}
    return render(request, 'core/lista_mensalidades.html', data)

@login_required
def aluno_novo(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_alunos')

@login_required
def mensalidade_novo(request):
    form = MensalidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalidades')

@login_required
def aluno_update(request, id):
    data = {}
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(request.POST or None, instance=aluno)
    data['aluno'] = aluno
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_alunos')
    else:
        return render(request, 'core/update_aluno.html', data)

@login_required
def mensalidade_update(request, id):
    data = {}
    mensalidade = Mensalidade.objects.get(id=id)
    form = MensalidadeForm(request.POST or None, instance=mensalidade)
    data['mensalidade'] = mensalidade
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalidades')
    else:
        return render(request, 'core/update_mensalidade.html', data)

@login_required
def aluno_detalhe(request, id):
    aluno = Aluno.objects.get(id=id)
    if request.method == 'POST':
        aluno.detalhe()
        return redirect('core_lista_alunos')
    else:
        return render(request, 'core/detail.html', {'aluno': aluno})

@login_required
def aluno_delete(request, id):
    aluno = Aluno.objects.get(id=id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('core_lista_alunos')
    else:
        return render(request, 'core/delete_confirm.html', {'aluno': aluno})

@login_required
def mensalidade_delete(request, id):
    mensalidade = Mensalidade.objects.get(id=id)
    if request.method == 'POST':
        mensalidade.delete()
        return redirect('core_lista_mensalidades')
    else:
        return render(request, 'core/delete_mensalidade_confirm.html', {'mensalidade': mensalidade})