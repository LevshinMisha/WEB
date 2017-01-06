from django.shortcuts import render, HttpResponse
import os
from .models import Comment, Like
from myauth.views import is_not_user
import xlwt
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
    Comment.objects.create(author=request.user, picture=filename, text=text)
    return HttpResponse('Надеюсь вы написали что-то умное')


def like(request, filename):
    if is_not_user(request):
        return HttpResponse('Залогинтесь, товарищъ')
    if len(Like.objects.filter(picture=filename, user=request.user)):
        Like.objects.get(picture=filename, user=request.user).delete()
        return HttpResponse('Лайк удален')
    Like.objects.create(picture=filename, user=request.user)
    return  HttpResponse('Лайк добавлен')


def get_likes(request, filename):
    return HttpResponse(len(Like.objects.filter(picture=filename)))


def get_xls(request):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    ws.write(0, 0, 'Имя файла')
    ws.write(0, 1, 'Кол-во комментариев')
    ws.write(0, 2, 'Кол-во лайков')
    urls = os.listdir(os.path.dirname(__file__)[:-8] + '/mysite/static/img')
    for i in range(len(urls)):
        ws.write(i + 1, 0, urls[i])
        ws.write(i + 1, 1, len(Comment.objects.filter(picture=i)))
        ws.write(i + 1, 2, len(Like.objects.filter(picture=i)))
    response = HttpResponse(content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=gallery.xls'
    wb.save(response)
    return response

