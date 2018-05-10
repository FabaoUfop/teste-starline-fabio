from rest_framework import serializers
from .models import Questao
from .models import User

class QuestaoSerializer (serializers.ModelSerializer):

    class Meta:
        model = Questao
        fields = ('usuario','questao_id','questao_area','questao_disciplina','questao_pergunta','questao_tipo','questao_objetiva','questao_discursiva')
#Classe responsavel por serializar os dados em uma API da model User

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
