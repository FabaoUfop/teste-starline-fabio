from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Questao,User
from .serializers import QuestaoSerializer, UserSerializer

from django.http import HttpResponse

# Create your views here

def index(request):
    questoes = Questao.objects.all()
    return render(request, 'questoes/index.html', {'questoes':questoes} )

def questoes(request):
    questoes = serialize("json", Questao.objects.all())
    return HttpResponse(questoes, content_type="application/json")

class QuestaoView (viewsets.ModelViewSet):
    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserView (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
