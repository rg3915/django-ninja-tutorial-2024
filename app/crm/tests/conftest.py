import pytest

from app.crm.models import Pessoa


@pytest.fixture
def user_data():
    return {
        'username': 'Lorem',
        'password': 'strong-test-pass',
    }


@pytest.fixture
def pessoa_data():
    return {
        'nome': 'Lorem',
        'idade': '20',
    }


@pytest.fixture
def test_password():
    return 'strong-test-pass'


@pytest.fixture
def user(django_user_model, user_data):
    """
    Cria usuário.
    """
    return django_user_model.objects.create_user(**user_data)


@pytest.fixture
def pessoa(django_user_model, pessoa_data):
    """
    Cria usuário.
    """
    return Pessoa.objects.create(**pessoa_data)
