from django.shortcuts import render


def cheater(request, title, message):
    return render(request, 'cheater.html', {'title': title, 'cheater_message': message})