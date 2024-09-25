from django.db import models
from core.models import User


class Compra(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name="Usuário")
    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    def __str__(self):
        return "Número do pedido: {}".format(self.id)

    class Meta:
        ordering = ["-id"]

    def total_quantity(self):
        return sum([item.quantity for item in self.itens.all()])



class Item(models.Model):
    compra = models.ForeignKey(
        Compra, on_delete=models.CASCADE, verbose_name="Compra", related_name="itens"
    )
    
    isbn = models.CharField("ISBN", max_length=13)
    title = models.CharField("Título", max_length=255)
    cover_i = models.CharField("Capa", max_length=255)
    author_name = models.CharField("Autor", max_length=255)
    subject = models.CharField("Assunto", max_length=255)
    publish_date = models.DateField("Data de publicação")
    first_sentence = models.TextField("Primeira frase")
    quantity = models.IntegerField("Quantidade")

    def __str__(self):
        return f"{self.title} : {self.quantity} unidade(s)"
