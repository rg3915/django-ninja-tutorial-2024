from http import HTTPStatus

import pytest


@pytest.mark.django_db
def test_login_sucesso(client, user_data, user):
    """
    Testa login.
    """
    path = '/api/v1/auth/login'
    response = client.post(path, user_data, content_type='application/json')
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_login_invalido(client, user):
    """
    Testa um login inválido.
    """
    path = '/api/v1/auth/login'

    user_data = {
        'username': 'Lorem',
        'password': 'senha-errada',
    }

    response = client.post(path, user_data, content_type='application/json')
    assert response.status_code == HTTPStatus.FORBIDDEN


@pytest.mark.django_db
def test_logout(client, user):
    path = '/api/v1/auth/logout'

    client.force_login(user)

    response = client.get(path)
    assert response.status_code == HTTPStatus.NO_CONTENT


@pytest.mark.django_db
def test_me(client, user):
    path = '/api/v1/users/me'

    client.force_login(user)

    response = client.get(path)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_request_reset_password(client):
    path = '/api/v1/users/me'
    data = {
        'email': 'test@example.com',
    }

    response = client.post(path, data, content_type='application/json')
    assert response.status_code == HTTPStatus.NO_CONTENT


@pytest.mark.django_db
def test_reset_password(client):
    ...


@pytest.mark.django_db
def test_change_password(client):
    ...
