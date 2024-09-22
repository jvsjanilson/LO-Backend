from django.contrib import admin
from core.models import Livro, Formapagamento
from compra.models import Compra, Item


admin.site.register(Formapagamento)


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItemInline]


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = (
        "isbn",
        "titulo",
        "autor",
        "numero_paginas",
        "categoria",
        "publicadora",
        "preco",
    )

    search_fields = ("titulo", "autor")
