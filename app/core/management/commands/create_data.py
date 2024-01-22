from dataclasses import asdict, dataclass
from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from app.crm.models import Pessoa

fake = Faker()


@dataclass
class PersonDTO:
    nome: str
    idade: int


def gen_person():
    nome = fake.name()
    idade = randint(16, 80)
    person_data = PersonDTO(nome=nome, idade=idade)
    return asdict(person_data)


def create_persons(number):
    aux = []
    for _ in range(number):
        data = gen_person()
        pessoa = Pessoa(**data)
        aux.append(pessoa)

    Pessoa.objects.bulk_create(aux)


class Command(BaseCommand):
    help = 'Gera dados randômicos para o model Pessoa.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', '-n', dest='number', type=int, help='Digite a quantidade de itens a serem gerados.'
        )

    def handle(self, *args, **options):
        number = options.get('number')

        if not number:
            number = 10

        create_persons(number)
