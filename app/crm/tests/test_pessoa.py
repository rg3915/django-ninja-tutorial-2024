import json
from http import HTTPStatus

import pytest

from app.crm.models import Pessoa


def get_token(client, user):
    data = {
        'username': user.username,
        'password': 'strong-test-pass',
    }

    response = client.post('/api/v1/token/pair', data, content_type='application/json')

    return json.loads(response.content)


@pytest.mark.django_db
def test_list_pessoas_with_token(client, user):
    """
    Testa o endpoint de um lista de pessoas, com JWT.
    Testa se retorna status_code 200.
    """
    client.force_login(user)

    token = get_token(client, user)

    headers = {'Authorization': f'Bearer {token["access"]}'}

    response = client.get('/api/v1/pessoas', headers=headers)

    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_detail_pessoa(client, user, pessoa):
    """
    Testa o endpoint dos detalhes de uma pessoa.
    Testa se retorna status_code 200.
    """
    client.force_login(user)

    token = get_token(client, user)

    headers = {'Authorization': f'Bearer {token["access"]}'}

    response = client.get(f'/api/v1/pessoas/{pessoa.slug}', headers=headers)

    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_create_pessoa(client, user, pessoa_data):
    """
    Testa a criação de uma instância de Pessoa através de uma requisição POST na API.
    """
    client.force_login(user)

    token = get_token(client, user)

    headers = {'Authorization': f'Bearer {token["access"]}'}

    response = client.post('/api/v1/pessoas', pessoa_data, content_type='application/json', headers=headers)

    pessoa = Pessoa.objects.first()

    expected = {
        'slug': str(pessoa.slug),
        'nome': 'Lorem',
        'idade': 20,
    }

    assert response.status_code == HTTPStatus.CREATED
    assert expected == json.loads(response.content)


@pytest.mark.django_db
def test_update_pessoa(client, user, pessoa, pessoa_data):
    """
    Testa a edição de uma Pessoa através de uma requisição PATCH na API.
    """
    client.force_login(user)

    token = get_token(client, user)

    headers = {'Authorization': f'Bearer {token["access"]}'}

    response = client.patch(
        f'/api/v1/pessoas/{pessoa.slug}', pessoa_data, content_type='application/json', headers=headers
    )

    expected = {
        'slug': str(pessoa.slug),
        'nome': 'Lorem',
        'idade': 20,
    }

    assert response.status_code == HTTPStatus.OK
    assert expected == json.loads(response.content)


@pytest.mark.django_db
def test_delete_pessoa(client, user, pessoa):
    """
    Testa se está deletando uma Pessoa.
    """
    client.force_login(user)

    token = get_token(client, user)

    headers = {'Authorization': f'Bearer {token["access"]}'}

    response = client.delete(f'/api/v1/pessoas/{pessoa.slug}', content_type='application/json', headers=headers)

    assert response.status_code == HTTPStatus.NO_CONTENT
