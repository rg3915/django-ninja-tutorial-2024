import uuid

from django.contrib.auth.models import User
from django.db import models


class UuidModel(models.Model):
    slug = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    criado_em = models.DateTimeField('criado em', auto_now_add=True, auto_now=False)
    modificado_em = models.DateTimeField('modificado em', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class CriadoPor(models.Model):
    criado_por = models.ForeignKey(
        User,
        verbose_name='criado por',
        related_name='%(app_label)s_%(class)s_criado_por',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class ModificadoPor(models.Model):
    modificado_por = models.ForeignKey(
        User,
        verbose_name='modificado por',
        related_name='%(app_label)s_%(class)s_modificado_por',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class AtivoModel(models.Model):
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class DefaultModel(UuidModel, TimeStampedModel, CriadoPor, ModificadoPor, AtivoModel):
    class Meta:
        abstract = True
