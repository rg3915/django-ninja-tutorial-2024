from django.contrib.auth import get_user_model
from ninja import Schema
from ninja.orm import create_schema

# from typing import Dict, List


UsernameSchemaMixin = create_schema(get_user_model(), fields=[get_user_model().USERNAME_FIELD])

EmailSchemaMixin = create_schema(get_user_model(), fields=[get_user_model().EMAIL_FIELD])

UserOutSchema = create_schema(get_user_model(), exclude=['password'])


class LoginSchema(UsernameSchemaMixin):
    password: str


class RequestPasswordResetSchema(EmailSchemaMixin):
    pass


class SetPasswordSchema(UsernameSchemaMixin):
    new_password1: str  # Não precisa
    new_password2: str  # Não precisa
    token: str


class ChangePasswordSchema(Schema):
    old_password: str
    new_password1: str
    new_password2: str


class ErrorsOutSchema(Schema):
    errors: dict[str, list[str]]
