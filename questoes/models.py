from django.db import models
from django.contrib.auth.models import User

#Model de questoes , ela possui relaçao 1:N com usuario


AREA = ( ('M',u'Medicas'),
         ('H',u'Humanas'),
         ('E',u'Exatas'),
         ('G',u'Gerenciais'),
        )
TIPO = (
        ('O',u'Objetiva'),
        ('D',u'Discursiva'),
        )
OPCOES = ( ('A',u'a'),
           ('B',u'b'),
           ('C',u'c'),
           ('D',u'd'),
        )
class Questao(models.Model):

    questao_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    questao_area = models.CharField(max_length=1,choices=AREA)
    questao_disciplina = models.CharField(max_length=40)
    questao_pergunta = models.CharField(max_length=100)
    questao_tipo = models.CharField(max_length=1, choices=TIPO)
    questao_objetiva = models.CharField(max_length=1,choices=OPCOES,null=True)
    questao_discursiva = models.TextField(max_length=100,null=True)

#lista questoes pelo filtro de perguntas

    class Meta:
        ordering = ["questao_pergunta"]
        verbose_name = u'Questao'

    def __str__(self):
        return self.pergunta

#classe com os dados de usuario

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_nome = models.CharField(max_length= 255)
    user_email = models.EmailField(max_length= 75)

    def __init__(self, arg):
        super(User, self).__init__()
        self.arg = arg
