from compra.models import Compra, Item
from core.models import Formapagamento
from rest_framework.serializers import ModelSerializer
from core.serializers import FormapagamentoSerializer
from rest_framework import serializers


class ItemSerializer(ModelSerializer):
    # livro = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    quantidade = serializers.IntegerField(required=True)

    class Meta:
        model = Item
        fields = "__all__"

    def validade_quantidade(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantidade inválida.")
        return value


class CompraSerializer(ModelSerializer):
    items = ItemSerializer(many=True, read_only=False)

    class Meta:
        model = Compra
        fields = ["user", "formapagamento", "items", "created_at"]

    def validate(self, attrs):

        if attrs["user"] != self.context["request"].user:
            raise serializers.ValidationError({"user": "Usuário inválido."})

        if not attrs["items"]:
            raise serializers.ValidationError({"items": "Compra sem itens."})

        return super().validate(attrs)

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        compra = Compra.objects.create(**validated_data)
        for item_data in items_data:
            Item.objects.create(compra=compra, **item_data)
        return compra
