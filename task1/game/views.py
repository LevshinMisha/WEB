from django.shortcuts import render, HttpResponse
from .models import Student, Player, Stage, Choice


def main(request):
    stage = current_player(request.user).cur_stage
    choices = Choice.objects.filter(stage_from=stage)
    return render(request, 'game.html', {'choices': choices, 'stage': stage})


def current_player(user):
    try:
        return Player.objects.get(user=user)
    except:
        return Player.objects.create(user=user, cur_stage=Stage.objects.get(code_name='StartPage'))


def next_stage(request, code_name):
    cur_player = current_player(request.user)
    choices = Choice.objects.filter(stage_from=cur_player.cur_stage)
    if code_name not in [i.stage_to.code_name for i in choices]:
        return HttpResponse('Читерок')
    new_stage = Stage.objects.get(code_name=code_name)
    cur_player.set_stage(new_stage)
    return HttpResponse(new_stage.dump_to_json())


