from django.db import models
from core.models import User


class Compra(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.RESTRICT, verbose_name="Usuário", null=True, blank=True
    )
    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    def __str__(self):
        return "Número do pedido: {}".format(self.id)

    class Meta:
        ordering = ["-id"]

    def total_quantity(self):
        return sum([item.quantity for item in self.itens.all()])


class Item(models.Model):
    compra = models.ForeignKey(
        Compra,
        on_delete=models.CASCADE,
        verbose_name="Compra",
        related_name="itens",
        null=True,
        blank=True,
    )

    isbn = models.CharField("ISBN", max_length=13)
    title = models.CharField(
        "Título", max_length=255, null=True, blank=True, default=""
    )
    cover_i = models.CharField(
        "Capa", max_length=255, null=True, blank=True, default=""
    )
    author_name = models.CharField("Autor", max_length=255, null=True, blank=True)
    subject = models.CharField(
        "Assunto", max_length=255, null=True, blank=True, default=""
    )
    publish_date = models.CharField(
        "Data de publicação", max_length=255, null=True, blank=True, default=""
    )
    first_sentence = models.TextField(
        "Primeira frase", null=True, blank=True, default=""
    )
    quantity = models.IntegerField("Quantidade")

    def __str__(self):
        return f"{self.title} : {self.quantity} unidade(s)"
