from django.shortcuts import render, HttpResponse
import os
from ipware.ip import get_ip
import json


ips = []
visits_count = 0

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


def popup(request):
    return render(request, 'popup.html', {'title': 'popup'})


def visits(request):
    global visits_count
    visits_count += 1
    if str(get_ip(request)) not in ips:
        ips.append(str(get_ip(request)))
    d = dict()
    d['unic_visits'] = len(ips)
    d['visits_count'] = visits_count
    return HttpResponse(json.dumps(d))