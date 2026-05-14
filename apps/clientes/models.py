from django.db import models

# Create your models here.

class cliente(models.Model):
    nome = models.CharField(verbose_name="Nome completo",max_length=100)
    cpf = models.CharField(verbose_name="CPF",max_length=14)
    telefone = models.CharField(verbose_name="TELEFONE", max_length=14)
    nascimento = models.DateField(verbose_name= "data de nascimento")

    def __str__(self): 
        return self.nome 