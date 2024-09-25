from django.db import models
from django.contrib.auth.models import AbstractUser
from core.choices import EstadosChoice
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

