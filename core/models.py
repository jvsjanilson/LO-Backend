from django.db import models
from django.contrib.auth.models import AbstractUser
from core.choices import EstadosChoice
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=150)
    endereco = models.CharField("Endereço", max_length=100)
    numero = models.CharField("Número", max_length=10)
    cep = models.CharField("CEP", max_length=8)
    complemento = models.CharField("Complemento", max_length=50, blank=True)
    bairro = models.CharField("Bairro", max_length=100)
    cidade = models.CharField("Cidade", max_length=100)
    estado = models.CharField(
        "Estado", max_length=2, choices=EstadosChoice.choices, default=EstadosChoice.RN
    )
    celular = models.CharField("Celular", max_length=11)

    def __str__(self):
        return self.username


class Formapagamento(models.Model):
    descricao = models.CharField("Descrição", max_length=100)

    def __str__(self):
        return self.descricao


class Livro(models.Model):
    isbn = models.CharField("ISBN", max_length=13, unique=True)
    titulo = models.CharField("Nome do livro", max_length=100)
    autor = models.CharField("Nome do autor", max_length=100)
    data_publicacao = models.DateField("Data de Publicação")
    capa_livro = models.ImageField("Capa do Livro", upload_to="capas/")
    numero_paginas = models.IntegerField(
        "Número de Páginas", validators=[MinValueValidator(1)]
    )
    categoria = models.CharField("Categoria", max_length=100)
    publicadora = models.CharField("Publicadora", max_length=100)
    sinopse = models.TextField("Sinopse", null=True, blank=True)
    preco = models.DecimalField("Preço", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo
