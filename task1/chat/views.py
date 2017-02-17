from django.shortcuts import render, HttpResponse
from .models import Message
import json


def main(request):
    Message.delete_old_messages()
    return render(request, 'chat.html')


def messages(request):
    Message.delete_old_messages()
    return HttpResponse(json.dumps([str(i) for i in Message.objects.all()]))


def add_message(request, text):
    Message.objects.create(text=text)
    Message.delete_old_messages()
    return HttpResponse('добавлено')
