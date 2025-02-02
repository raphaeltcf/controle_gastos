from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criação = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
class transacoes(models.Model):
    data = models.DateTimeField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    descricao = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural: "transações"

    def __str__(self):
        return self.descricao
# Create your models here.
