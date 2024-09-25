from compra.models import Compra, Item
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

    

class CompraSerializer(ModelSerializer):
    items = ItemSerializer(many=True, read_only=False)

    class Meta:
        model = Compra
        fields = ["user", "items", "created_at"]

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
