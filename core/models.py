from django.db import models

class Aluno(models.Model):
    FAIXA = (
        ('BRANCA', 'Branca'),
        ('CINZA', 'Cinza'),
        ('AMARELA', 'Amarela'),
        ('LARANJA', 'Laranja'),
        ('VERDE', 'Verde'),
        ('AZUL', 'Azul'),
        ('ROXA', 'Roxa'),
        ('MARROM', 'Marrom'),
        ('PRETA', 'Preta'),
    )

    STATUS = (
        ('ATIVO', 'Ativo'),
        ('ENCERRADO', 'Encerrado'),
        ('TRANCADO', 'Trancado'),

    )
    nome = models.CharField(max_length=100, verbose_name="Nome")
    faixa = models.CharField(max_length=100, choices=FAIXA, verbose_name="Graduação")
    datagraduacao = models.DateTimeField(verbose_name="Data Graduação")
    datanascimento = models.DateTimeField(verbose_name="Data Nascimento")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    status = models.CharField(max_length=100, choices=STATUS, verbose_name="Status Aluno")
    observacao = models.CharField(max_length=100, verbose_name="Observação")

    def __str__(self):
        return self.nome

class Mensalidade(models.Model):
    MESES_ANO = (
        ('JANEIRO', 'Janeiro'),
        ('FEVEREIRO', 'Fevereiro'),
        ('MARÇO', 'Março'),
        ('ABRIL', 'Abril'),
        ('MAIO', 'Maio'),
        ('JUNHO', 'Junho'),
        ('JULHO', 'Julho'),
        ('AGOSTO', 'Agosto'),
        ('SETEMBRO', 'Setembro'),
        ('OUTUBRO', 'Outubro'),
        ('NOVEMBRO', 'Novembro'),
        ('DEZEMBRO', 'Dezembro'),

 )

    CATEGORIA = (
        ('CRIANCA', 'Crianca'),
        ('ADULTO', 'Adulto'),

 )

    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE, verbose_name="Aluno")
    mes = models.CharField(max_length=100, choices=MESES_ANO, verbose_name="Mês")
    dataPagamento = models.DateTimeField(verbose_name="Data de Pagamento")
    valorPago = models.CharField(max_length=20, verbose_name="Valor Pago" )
    categoria = models.CharField(max_length=100, choices=CATEGORIA, verbose_name="Categoria")

    def __str__(self):
        return self.aluno.nome + ' - ' + self.mes
