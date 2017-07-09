from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .form import LoginForm, RegistrationForm
from .settings import PAGE_TO_REDIRECT_AFTER_AUTH
from .models import RegistrationRequest
from utils.views import cheater


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
            return cheater(request, 'Регистрация', form.registrate())
    return render(request, "registration.html", {'form': RegistrationForm(), 'title': 'Регистрация'})


def create_user(request, username, token):
    if len(RegistrationRequest.objects.filter(username=username, token=token)):
        user = RegistrationRequest.objects.get(username=username, token=token).create_real_user()
        login(request, user)
        RegistrationRequest.objects.get(username=username, token=token).delete()
        return cheater(request, 'Регистрация завершена', 'Надеюсь вы не угадали свой токен! Добро пожаловать!')
    return cheater(request, 'Регистрация провалилась', 'Пытались угадать токен? Так вот - вы ошиблись!')