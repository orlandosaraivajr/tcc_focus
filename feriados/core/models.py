from django.db import models

class FeriadoModel(models.Model):
    nome = models.CharField('Feriado',max_length=50)
    data = models.DateField('Data')

    def __str__(self):
        return self.nome
