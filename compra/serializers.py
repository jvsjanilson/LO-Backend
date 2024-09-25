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
    total_items = serializers.SerializerMethodField()
    items_create = ItemSerializer(many=True, write_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Compra
        fields = ["id", "user", "created_at", "total_items", "items", "items_create"]

    def validate(self, attrs):

        if not attrs["items_create"]:
            raise serializers.ValidationError({"items": "Compra sem itens."})

        return super().validate(attrs)

    def create(self, validated_data):
        items_data = validated_data.pop("items_create")
        compra = Compra.objects.create(**validated_data)
        for item_data in items_data:
            Item.objects.create(compra=compra, **item_data)
        return compra

    def get_items(self, obj):
        items = obj.itens.all()
        return ItemSerializer(items, many=True).data

    def get_total_items(self, obj):
        return sum([item.quantity for item in obj.itens.all()])
