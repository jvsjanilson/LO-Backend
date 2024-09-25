from compra.models import Compra, Item
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "isbn",
            "title",
            "cover_i",
            "author_name",
            "subject",
            "publish_date",
            "first_sentence",
            "quantity",
        ]

    

class CompraSerializer(ModelSerializer):
    items = serializers.SerializerMethodField()
    # items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ["id", "user",  "created_at", "items"]

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

    def get_items(self, obj):
        items = obj.itens.all()
        return ItemSerializer(items, many=True).data