from django.db import models

from app.core.models import DefaultModel


class Pessoa(DefaultModel):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()

    class Meta:
        ordering = ('nome',)
        verbose_name = 'pessoa'
        verbose_name_plural = 'pessoas'

    def __str__(self):
        return self.nome
