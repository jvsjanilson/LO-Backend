from rest_framework.serializers import ModelSerializer
from core.models import Livro, Formapagamento


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"


class FormapagamentoSerializer(ModelSerializer):
    class Meta:
        model = Formapagamento
        fields = "__all__"
