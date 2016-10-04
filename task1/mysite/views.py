from django.shortcuts import render
import os, os.path as path


def main_page(request):
    return render(request, 'main.html', {'title': 'Кто здесь?'})


def contacts(request):
    return render(request, 'contacts.html', {'title': "Контактики"})


def about(request):
    return render(request, 'about.html', {'title': 'О Царе'})


def links(request):
    return render(request, 'links.html', {'title': "Ссылочки"})


def gallery(request):
    urls = ['/static/img/' + filename for filename in os.listdir(os.path.dirname(__file__) + '/static/img')]
    return render(request, 'gallery.html', {'title': 'Картиночки', 'urls': urls})