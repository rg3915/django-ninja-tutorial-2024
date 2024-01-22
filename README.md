# django-ninja-tutorial-2024

Django Ninja Tutorial 2024

## Este projeto foi feito com:

* [Python 3.11.7](https://www.python.org/)
* [Django 5.0.1](https://www.djangoproject.com/)
* [Django-Ninja 1.0.1](https://django-ninja.rest-framework.com/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
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