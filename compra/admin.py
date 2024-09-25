from django.contrib import admin
from compra.models import Compra, Item


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

