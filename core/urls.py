from django.conf.urls import url, include

from .views import (home, lista_alunos, lista_mensalidades,
                    aluno_novo, mensalidade_novo,
                    aluno_update, mensalidade_update,
                    aluno_delete, mensalidade_delete,
                    aluno_detalhe, mensalidade_detalhe,
                    conta_novo, conta_update, conta_delete,
                    conta_detalhe, lista_contas
)


urlpatterns = [
    url(r'^$', home, name ='core_home'),

    url(r'^alunos/$', lista_alunos, name='core_lista_alunos'),
    url(r'^aluno-novo/$', aluno_novo, name='core_aluno_novo'),
    url(r'^aluno-update/(?P<id>\d+)/$', aluno_update, name='core_aluno_update'),
    url(r'^aluno-delete/(?P<id>\d+)/$', aluno_delete, name='core_aluno_delete'),
    url(r'^aluno-detalhe/(?P<id>\d+)/$', aluno_detalhe, name='core_aluno_detalhe'),

    url(r'^mensalidades/$', lista_mensalidades, name='core_lista_mensalidades'),
    url(r'^mensalidades-novo/$', mensalidade_novo, name='core_mensalidade_novo'),
    url(r'^mensalidade-update/(?P<id>\d+)/$', mensalidade_update, name='core_mensalidade_update'),
    url(r'^mensalidade-delete/(?P<id>\d+)/$', mensalidade_delete, name='core_mensalidade_delete'),
    url(r'^mensalidade-detalhe/(?P<id>\d+)/$', mensalidade_detalhe, name='core_mensalidade_detalhe'),

    url(r'^contas/$', lista_contas, name='core_lista_contas'),
    url(r'^contas-novo/$', conta_novo, name='core_conta_novo'),
    url(r'^conta-update/(?P<id>\d+)/$', conta_update, name='core_conta_update'),
    url(r'^conta-delete/(?P<id>\d+)/$', conta_delete, name='core_conta_delete'),
    url(r'^conta-detalhe/(?P<id>\d+)/$', conta_detalhe, name='core_conta_detalhe'),
]