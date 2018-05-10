from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Questao

class ModelTestCase(TestCase):
    """Essa classe é uma classe de testes."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.questoes_name = "Write world class code"
        self.questaolist = QuestaoList(name=self.questaolist_name)

    def test_model_can_create_a_bucketlist(self):
        """Testa a bucketlist na model Questao na criação da lista de perguntas(quantidade)."""

        old_count = QuestaoList.objects.count()
        self.questaolist.save()
        new_count = QuestaoList.objects.count()
        self.assertNotEqual(old_count, new_count)
