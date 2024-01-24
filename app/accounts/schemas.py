from django.contrib.auth import get_user_model
from ninja import Schema, Field
from ninja.orm import create_schema


UsernameSchemaMixin = create_schema(get_user_model(), fields=[get_user_model().USERNAME_FIELD])

EmailSchemaMixin = create_schema(get_user_model(), fields=[get_user_model().EMAIL_FIELD])

UserOutSchema = create_schema(get_user_model(), exclude=['password'])


class LoginSchema(UsernameSchemaMixin):
    password: str


class RequestPasswordResetSchema(EmailSchemaMixin):
    pass


class SetPasswordSchema(UsernameSchemaMixin):
    new_password1: str = Field(..., min_length=8)
    new_password2: str = Field(..., min_length=8)
    token: str

    # https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.model_validator


class ChangePasswordSchema(Schema):
    old_password: str
    new_password1: str
    new_password2: str


class ErrorsOutSchema(Schema):
    errors: dict[str, list[str]]
