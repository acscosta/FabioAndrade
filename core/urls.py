from django.conf.urls import url, include

from .views import (home, lista_alunos, lista_mensalidades,
                    aluno_novo, mensalidade_novo,
                    aluno_update, mensalidade_update,
                    aluno_delete, mensalidade_delete,
                    aluno_detalhe
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


]