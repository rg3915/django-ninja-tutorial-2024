# django-ninja-tutorial-2024

Django Ninja Tutorial 2024

https://django-ninja.dev/

## O que o projeto faz?

* Autenticação
    * Login
    * Logout
    * Reset de Senha
    * Troca de Senha
    * JWT

* Exemplo de CRUD
    * Criar Pessoa
    * Ler Pessoa
    * Editar Pessoa
    * Deletar Pessoa

## Este projeto foi feito com:

* [Python 3.11.7](https://www.python.org/)
* [Django 5.0.1](https://www.djangoproject.com/)
* [Django-Ninja 1.0.1](https://django-ninja.dev/)


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```bash
git clone https://github.com/rg3915/django-ninja-tutorial-2024.git
cd django-ninja-tutorial-2024

python -m venv .venv
source .venv/bin/activate

pip install -r requirements/dev.txt

python contrib/env_gen.py

python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""

pytest -vv
```

## url da doc

A doc é gerada automaticamente com Swagger.

http://localhost:8000/api/v1/docs


## Usando httpie para fazer as requisições pelo terminal

```
pip install httpie
```

Requisição

```bash
http post http://localhost:8000/api/v1/users/request_reset_password email=nome@email.com

http post http://localhost:8000/api/v1/users/reset_password \
username=nome \
new_password1=demodemo \
new_password2=demodemo \
token=c1adg7...
```


## Obtendo token para JWT

Para usar a autenticação JWT, é necessário gerar um token a partir de:

```bash
curl -X 'POST' \
  -H 'accept: application/json' \
  -d '{"username": "seu-username", "password": "sua-senha"}' \
  'http://localhost:8000/api/v1/token/pair'
```

Você vai obter um `access` token

```json
{"username": "seu-username", "refresh": "eyJhbGc...meqMzc", "access": "eyJhbGc...efk0U"}
```

Pegue o `access` e combine com `Bearer` para autenticar:


```bash
curl -X GET \
http://localhost:8000/api/v1/persons \
-H 'Authorization: Bearer eyJhbGciOiJIUzI7N...'
```

## Estrutura do projeto

```
.
├── app
│   ├── accounts
│   │   ├── api.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── __init__.py
│   │   ├── schemas.py
│   │   └── tests
│   │       ├── conftest.py
│   │       ├── __init__.py
│   │       └── test_accounts.py
│   ├── api.py
│   ├── asgi.py
│   ├── core
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── management
│   │   │   ├── commands
│   │   │   │   ├── create_data.py
│   │   │   │   ├── __init__.py
│   │   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── services
│   │   │   ├── email.py
│   │   │   └── __init__.py
│   │   └── utils
│   │       ├── helpers.py
│   │       ├── __init__.py
│   │       └── validators.py
│   ├── crm
│   │   ├── admin.py
│   │   ├── api.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── tests
│   │       ├── conftest.py
│   │       ├── __init__.py
│   │       └── test_pessoa.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── contrib
│   └── env_gen.py
├── Makefile
├── manage.py
├── pyproject.toml
├── pytest.ini
├── README.md
├── requirements
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── requirements.txt
└── ruff.toml
```

## Links

https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.model_validator

