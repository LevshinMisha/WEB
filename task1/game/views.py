from django.shortcuts import render, HttpResponse
from .models import Student

def main(request):
    return render(request, 'game.html')
