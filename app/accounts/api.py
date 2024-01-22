from http import HTTPStatus

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, update_session_auth_hash
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from ninja import Router
from ninja.security import django_auth

from .schemas import (
    ChangePasswordSchema,
    ErrorsOutSchema,
    LoginSchema,
    RequestPasswordResetSchema,
    SetPasswordSchema,
    UserOutSchema,
)

router = Router()

# TODO
_LOGIN_BACKEND = 'django.contrib.auth.backends.ModelBackend'


@router.post(
    'auth/login', response={HTTPStatus.OK: UserOutSchema, HTTPStatus.FORBIDDEN: None}, auth=None, tags=['Auth']
)  # noqa E501
def login(request, data: LoginSchema):
    user = authenticate(backend=_LOGIN_BACKEND, **data.dict())

    if user is not None and user.is_active:
        django_login(request, user, backend=_LOGIN_BACKEND)
        return user

    return HTTPStatus.FORBIDDEN, None


@router.get('auth/logout', response={HTTPStatus.NO_CONTENT: None}, auth=django_auth, tags=['Auth'])
def logout(request):
    django_logout(request)
    return HTTPStatus.NO_CONTENT, None


@router.get('users/me', response=UserOutSchema, auth=django_auth, tags=['Users'])
def me(request):
    return request.user


@router.post('users/request_reset_password', response={HTTPStatus.NO_CONTENT: None}, auth=None, tags=['Users'])
def request_reset_password(request, data: RequestPasswordResetSchema):
    """
    Use este endpoint para enviar e-mail ao usuário com link para reset de senha.
    """
    form = PasswordResetForm(data.dict())
    if form.is_valid():
        form.save(
            request=request,
            extra_email_context=(
                {'frontend_url': settings.FRONTEND_URL} if hasattr(settings, 'FRONTEND_URL') else None
            ),
        )
    return HTTPStatus.NO_CONTENT, None


@router.post(
    'users/reset_password',
    response={
        HTTPStatus.OK: UserOutSchema,
        HTTPStatus.FORBIDDEN: ErrorsOutSchema,
        HTTPStatus.UNPROCESSABLE_ENTITY: None,
    },
    auth=None,
    tags=['Users'],
)
def reset_password(request, data: SetPasswordSchema):
    """
    Use este endpoint para finalizar o processo de reset de senha.

    Este endpoint não é uma URL que será diretamente exposta aos usuários,
    você deve fornecer um site em seu app frontend que enviará uma requisição POST
    para o endpoint de confirmação de reset de senha.
    """
    user_field = get_user_model().USERNAME_FIELD
    user_data = {user_field: getattr(data, user_field)}
    user = get_user_model().objects.filter(**user_data)

    if user.exists():
        user = user.get()
        if default_token_generator.check_token(user, data.token):
            form = SetPasswordForm(user, data.dict())
            if form.is_valid():
                form.save()
                django_login(request, user, backend=_LOGIN_BACKEND)
                return user
            return HTTPStatus.FORBIDDEN, {'errors': dict(form.errors)}
    return HTTPStatus.UNPROCESSABLE_ENTITY, None


@router.post(
    'users/change_password',
    response={HTTPStatus.OK: None, HTTPStatus.FORBIDDEN: ErrorsOutSchema},
    auth=django_auth,
    tags=['Users'],
)
def change_password(request, data: ChangePasswordSchema):
    """
    Use este endpoint para redefinir a senha.
    """
    form = PasswordChangeForm(request.user, data.dict())
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, request.user)
        return HTTPStatus.OK
    return HTTPStatus.FORBIDDEN, {'errors': dict(form.errors)}
