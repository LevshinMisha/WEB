from myauth.utils import is_not_user

from django.shortcuts import HttpResponse


def authorized_users_only(func):
    def f(request, *args, **kwargs):
        if is_not_user(request):
            return HttpResponse('Залогинтесь, товарищъ')
        return func(request, *args, **kwargs)
    return f


def ajax_only(func):
    def f(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponse('По этой ссылке можно пройти только через ajax запрос')
        return func(request, *args, **kwargs)
    return f