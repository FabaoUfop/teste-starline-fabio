from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers
import requests

router = routers.DefaultRouter()
router.register('questoes', views.QuestaoView)
router.register('user', views.UserView)

urlpatterns = [
    path('app/', include(router.urls)),
    url(r'^$', views.index, name="index"),
    url(r'^questoes/questao$', views.questoes, name="questoes")
]
