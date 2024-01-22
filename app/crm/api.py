from http import HTTPStatus

from django.shortcuts import get_object_or_404
from ninja import Query, Router
from ninja.pagination import paginate
from ninja_jwt.authentication import JWTAuth

from app.crm.models import Pessoa
from app.crm.schemas import PessoaCreateSchema, PessoaFilterSchema, PessoaSchema

router = Router(tags=['Pessoas'])


@router.get('pessoas', response=list[PessoaSchema], auth=JWTAuth())
@paginate
def list_person(request, filters: PessoaFilterSchema = Query(...)):
    pessoas = Pessoa.objects.all()
    pessoas = filters.filter(pessoas)
    return pessoas


@router.get('pessoas/{slug}', response=PessoaSchema, auth=JWTAuth())
def detail_person(request, slug: str):
    return get_object_or_404(Pessoa, slug=slug)


@router.post('pessoas', response={HTTPStatus.CREATED: PessoaSchema}, auth=JWTAuth())
def create_person(request, payload: PessoaCreateSchema):
    return Pessoa.objects.create(**payload.dict())


@router.patch('pessoas/{slug}', response=PessoaSchema, auth=JWTAuth())
def update_person(request, slug: str, payload: PessoaCreateSchema):
    instance = get_object_or_404(Pessoa, slug=slug)
    data = payload.dict()

    for attr, value in data.items():
        setattr(instance, attr, value)

    instance.save()
    return instance


@router.delete('pessoas/{slug}', response={HTTPStatus.NO_CONTENT: None})  # , auth=JWTAuth()
def delete_person(request, slug: str):
    instance = get_object_or_404(Pessoa, slug=slug)
    instance.delete()
    return HTTPStatus.NO_CONTENT, None
