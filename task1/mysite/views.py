from django.shortcuts import render, HttpResponse
import os

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
    urls = [(urls[i], i) for i in range(len(urls))]
    return render(request, 'gallery.html', {'title': 'Картиночки', 'urls': urls})


def popup(request):
    return render(request, 'popup.html', {'title': 'popup'})