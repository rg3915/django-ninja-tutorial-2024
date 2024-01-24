import pytest


@pytest.fixture
def user_data():
    return {
        'username': 'lorem',
        'email': 'test@example.com',
        'password': 'strong-test-pass',
    }


@pytest.fixture
def user(django_user_model, user_data):
    """
    Cria usuário.
    """
    return django_user_model.objects.create_user(**user_data)
