from django.shortcuts import render, HttpResponse
import os
from .models import Comment
from myauth.views import is_not_user
import json


def gallery(request):
    urls = os.listdir(os.path.dirname(__file__)[:-8] + '/mysite/static/img')
    urls = ['/static/img/thumbnails/' + filename for filename in urls if filename != 'thumbnails']
    urls = [(urls[i][:-4] + '_tn.jpg', i) for i in range(len(urls))]
    return render(request, 'gallery.html', {'title': 'Картиночки', 'urls': urls})


def get_comments(request, filename):
    return HttpResponse(json.dumps({'comments': [i.to_json() for i in Comment.objects.filter(picture=filename)]}))


def add_comment(request, filename, text):
    if is_not_user(request):
        return HttpResponse('Залогинтесь, товарищъ')
    if len(text) > 300:
        return HttpResponse('Многа букаф неасилил :(')
    for i in text.split(' '):
        if len(i) > 20:
            return HttpResponse('Какие длинные и не понятные слова. Попытались выглядить умнее?')
    if len(Comment.objects.filter(author=request.user, picture=filename, text=text)):
        return HttpResponse('Повторюша, дядя Хрюша')
    if len(Comment.objects.filter(picture=filename)) > 3:
        return HttpResponse('Место под комментарии закончилось.')
    Comment.objects.create(author=request.user, picture=filename, text=text)
    return HttpResponse('Надеюсь вы написали что-то умное')


