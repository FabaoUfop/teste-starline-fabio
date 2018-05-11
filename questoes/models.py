from django.db import models
from django.contrib.auth.models import User

#Model de questoes , ela possui relaçao 1:N com usuario




TIPO = (
        ('MB',u'Multipla Escolha'),
        ('D',u'Discursiva'),
        )
ENSINO = ( ('ES',u'Ensino Superior'),
         ('EB',u'Ensino (Fundamental e Médio)'),
         ('ET',u'Ensino Técnico'),
        )
OPCOES = ( ('A',u'a'),
           ('B',u'b'),
           ('C',u'c'),
           ('D',u'd'),
        )
class Questao(models.Model):

    questao_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_questao = models.CharField(max_length=2, choices=TIPO)
    questao_ensino = models.CharField(max_length=2,choices=ENSINO)
    questao_disciplina = models.CharField(max_length=40)
    questao_enunciado = models.TextField(max_length=100)
    questao_objetiva = models.CharField(max_length=1,choices=OPCOES,null=True, blank=True)
    questao_discursiva = models.TextField(max_length=100,null=True, blank=True)

#lista questoes pelo filtro de perguntas

    class Meta:
        ordering = ["questao_enunciado"]
        verbose_name = u'Questao'

    def __str__(self):
        return self.questao_pergunta
