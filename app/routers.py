from rest_framework import routers
from questoes.viewsets import QuestaoViewSet

router = routers.DefaultRouter()
router.register(r'questoes', QuestaoViewSet)
