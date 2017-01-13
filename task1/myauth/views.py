from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
from .form import LoginForm, RegistrationForm
from .settings import PAGE_TO_REDIRECT_AFTER_AUTH, AUTH_PAGE
from .models import RegistrationRequest


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
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return render(request, 'cheater.html', {'title': 'Регистрация', 'cheater_message': form.registrate()})
    return render(request, "registration.html", {'form': RegistrationForm(), 'title': 'Регистрация'})


def create_user(request, username, token):
    if len(RegistrationRequest.objects.filter(username=username, token=token)):
        user = RegistrationRequest.objects.get(username=username, token=token).create_real_user()
        login(request, user)
        RegistrationRequest.objects.get(username=username, token=token).delete()
        return render(request, 'cheater.html', {'title' : 'Регистрация завершена', 'cheater_message': 'Надеюсь вы не угадали свой токен! Добро пожаловать!'})
    return render(request, 'cheater.html', {'title': 'Регистрация провалилась', 'cheater_message': 'Пытались угадать токен? Так вот - вы ошиблись! Попробуйте еще раз!'})