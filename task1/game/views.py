from django.shortcuts import render, HttpResponse
from .models import Student, Player, Stage, Choice
from myauth.views import need_authentication


@need_authentication
def main(request):
    return render(request, 'game.html')


def current_player(user):
    try:
        return Player.objects.get(user=user)
    except:
        return Player.objects.create(user=user, cur_stage=Stage.objects.get(codename='StartPage'))


def next_stage(request, codename):
    cur_player = current_player(request.user)
    choices = Choice.objects.filter(stage_from=cur_player.cur_stage)
    if codename not in [i.stage_to.codename for i in choices]:
        return HttpResponse('Читерок')
    cur_player.set_stage(Stage.objects.get(codename=codename))
    return HttpResponse('Ок')


def current_stage(request):
    return HttpResponse(str(current_player(request.user).cur_stage))


def get_stage(request, codename):
    return HttpResponse(Stage.objects.get(codename=codename).dump_to_json())


