from django.db import models
from core.models import User, Livro, Formapagamento


class Compra(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name="Usuário")
    formapagamento = models.ForeignKey(
        Formapagamento,
        on_delete=models.RESTRICT,
        verbose_name="Forma de Pagamento",
    )
    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    def __str__(self):
        return "Número do pedido: {}".format(self.id)

    class Meta:
        ordering = ["-id"]

    #     return f"{self.created_at} - {self.items.livro.preco  * self.items.quantidade}"


class Item(models.Model):
    compra = models.ForeignKey(
        Compra, on_delete=models.CASCADE, verbose_name="Compra", related_name="itens"
    )
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name="Livro")
    quantidade = models.IntegerField("Quantidade")

    def __str__(self):
        return f"{self.livro.titulo} : {self.quantidade} - {self.quantidade * self.livro.preco}"

    def subtotal(self):
        return self.quantidade * self.livro.preco
