from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user_model
import os


def main_page(request):
    return render(request, 'main.html', {'title': 'Кто здесь?'})


def contacts(request):
    return render(request, 'contacts.html', {'title': "Контактики"})


def about(request):
    return render(request, 'about.html', {'title': 'О Царе'})


def links(request):
    return render(request, 'links.html', {'title': "Ссылочки"})


def ban(request):
    from django.core.mail import send_mail

    send_mail('Subject here', 'Here is the message.', 'xTave@yandex.ru',
              ['mishalevshin@gmail.com'], fail_silently=False)
    return HttpResponse('Все неверные забанены')


def redirect_to_main(request):
    return redirect('/main/')