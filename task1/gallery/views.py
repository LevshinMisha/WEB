from django.shortcuts import render, HttpResponse
import os
from .models import Comment, Like
from utils.decorators import authorized_users_only, ajax_only
import xlwt
import json


def gallery(request):
    urls = os.listdir(os.path.dirname(__file__)[:-8] + '/mysite/static/img')
    urls = ['/static/img/thumbnails/' + filename for filename in urls if filename != 'thumbnails']
    urls = [(urls[i][:-4] + '_tn.jpg', i) for i in range(len(urls))]
    return render(request, 'gallery.html', {'title': 'Картиночки', 'urls': urls})


@ajax_only
def get_comments(request, filename):
    return HttpResponse(json.dumps({'comments': [i.json() for i in Comment.objects.filter(picture=filename)]}))


@ajax_only
@authorized_users_only
def add_comment(request, filename, text):
    if len(text) > 300:
        return HttpResponse('Многа букаф неасилил :(')
    Comment.objects.create(author=request.user, picture=filename, text=text.replace(' /n', '\n').replace(' /q', '?'))
    return HttpResponse('Надеюсь вы написали что-то умное')


@ajax_only
@authorized_users_only
def like(request, filename):
    if len(Like.objects.filter(picture=filename, user=request.user)):
        Like.objects.get(picture=filename, user=request.user).delete()
        return HttpResponse('Лайк удален')
    Like.objects.create(picture=filename, user=request.user)
    return HttpResponse('Лайк добавлен')


@ajax_only
def get_likes(request, filename):
    return HttpResponse(len(Like.objects.filter(picture=filename)))


def get_xls(request):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Галерея')
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

