from rest_framework import serializers
from .models import Questao
from .models import User

class QuestaoSerializer (serializers.ModelSerializer):

    class Meta:
        model = Questao
        #depth = 1
        fields = '__all__'
#Classe responsavel por serializar os dados em uma API da model User

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        #depth = 1
        fields = '__all__'
