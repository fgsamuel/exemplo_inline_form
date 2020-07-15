from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, blank=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=CASCADE, related_name='telefones')
    numero = models.CharField(max_length=11)

    def __str__(self):
        return self.numero
