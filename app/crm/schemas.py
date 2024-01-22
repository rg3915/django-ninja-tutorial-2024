from typing import Optional

from ninja import Field, FilterSchema, ModelSchema

from app.crm.models import Pessoa


class PessoaSchema(ModelSchema):
    class Meta:
        model = Pessoa
        fields = ('slug', 'nome', 'idade')


class PessoaFilterSchema(FilterSchema):
    nome: Optional[str] = Field(None, q='nome__icontains')


class PessoaCreateSchema(ModelSchema):
    class Meta:
        model = Pessoa
        fields = (
            'nome',
            'idade',
        )
