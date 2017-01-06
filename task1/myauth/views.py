from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
from .form import LoginForm, RegistrationForm
from .settings import PAGE_TO_REDIRECT_AFTER_AUTH, AUTH_PAGE


def is_not_user(request):
    return not isinstance(request.user, get_user_model())


def is_admin(request):
    return not is_not_user(request) and request.user.is_superuser


def need_authentication(func):
    def f(request, *args, **kwargs):
        if is_not_user(request):
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
    #  return render(request, 'cheater.html', {'title': 'Читерок', 'cheater_message': 'Регистрация закрыта, но вы держитесь'})
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.registrate()
            login(request, user)
            return redirect(PAGE_TO_REDIRECT_AFTER_AUTH)
    form = RegistrationForm()
    return render(request, "registration.html", {'form': form, 'title': 'Регистрация'})
