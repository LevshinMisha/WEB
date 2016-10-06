from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
from .form import LoginForm, RegistrationForm
from .settings import PAGE_TO_REDIRECT_AFTER_AUTH, AUTH_PAGE
from ipware.ip import get_real_ip, get_ip, get_trusted_ip

ips = []


def is_user(request):
    return not isinstance(request.user, get_user_model())


def is_admin(request):
    return is_user(request) and request.user.is_superuser


def admin_can_do_it(f):
    def func(request, *args, **kwargs):
        if is_admin(request):
            return lambda: True
        else:
            return f
    return func


def need_authentication(func):
    def f(request, *args, **kwargs):
        if is_user(request):
            return redirect(AUTH_PAGE)
        return func(request, *args, **kwargs)
    return f


def log_out(request):
    logout(request)
    return redirect(PAGE_TO_REDIRECT_AFTER_AUTH)


def auth(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.authenticate()
            if user is not None and user.is_active:
                login(request, user)
                return redirect(PAGE_TO_REDIRECT_AFTER_AUTH)
    form = LoginForm()
    return render(request, 'auth.html', {'form': form, 'title': 'Авторизация'})


def register(request):
    if request.method == "POST":
        for i in ips:
            if str(get_ip(request)) == i:
                return render(request, "cheater.html",
                              {'title': 'Читерок', 'cheater_message': 'Пытались зарегистрироваться дважды?'})
        form = RegistrationForm(request.POST)
        if form.is_valid():
            ips.append(str(get_ip(request)))
            user = form.registrate()
            login(request, user)
            return redirect(PAGE_TO_REDIRECT_AFTER_AUTH)
    form = RegistrationForm()
    return render(request, "registration.html", {'form': form, 'title': 'Регистрация'})
