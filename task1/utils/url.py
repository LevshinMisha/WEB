from django.shortcuts import redirect


def redirect_to(to):
    return lambda r: redirect(to)