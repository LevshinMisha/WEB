from django.contrib.auth import get_user_model
from django.shortcuts import redirect

from .settings import AUTH_PAGE


def is_not_user(request):
    return not is_user(request)


def is_user(request):
    return isinstance(request.user, get_user_model())


def is_admin(request):
    return is_user(request) and request.user.is_superuser


def authorized_users_only(func):
    def f(request, *args, **kwargs):
        if is_not_user(request):
            return redirect(AUTH_PAGE)
        return func(request, *args, **kwargs)
    return f