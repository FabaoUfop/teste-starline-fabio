from django.shortcuts import render
from rest_framework import viewsets

from .models import Questao,User
from .serializers import QuestaoSerializer, UserSerializer

# Create your views here

class QuestaoView (viewsets.ModelViewSet):
    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer

class UserView (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
