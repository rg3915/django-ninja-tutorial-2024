# django-ninja-tutorial-2024

Django Ninja Tutorial 2024

## Este projeto foi feito com:

* [Python 3.11.7](https://www.python.org/)
* [Django 5.0.1](https://www.djangoproject.com/)
* [Django-Ninja 1.0.1](https://django-ninja.rest-framework.com/)
* [Django Rest Framework 3.14.0](https://www.django-rest-framework.org/)
* [Bootstrap 5.0](https://getbootstrap.com/)
* [VueJS 3.2.13](https://vuejs.org/)
* [AlpineJS](https://alpinejs.dev/)
* [htmx](https://htmx.org)
* [jQuery 3.4.1](https://jquery.com/)

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