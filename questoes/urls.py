from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('Questoes', views.QuestaoView)
router.register('User', views.UserView)

urlpatterns = [
    path('', include(router.urls))
]