from django.shortcuts import render, HttpResponse
import os
from ipware.ip import get_ip
import json
from django.contrib.auth import get_user_model
from .models import UserDayVisits, Day
from django.utils import timezone


def today_already_exists():
    return len(Day.objects.filter(date=timezone.now()))


def user_already_visit_in_this_day(user, day):
    if isinstance(user, get_user_model()):
        return len(UserDayVisits.objects.filter(user=user, day=day))
    return True


def visits(request):
    visits_count = 0
    user = request.user
    if today_already_exists():
        day = Day.objects.get(date=timezone.now())
    else:
        day = Day.objects.create()
    if not user_already_visit_in_this_day(user, day):
        UserDayVisits.objects.create(user=user, day=day)
    if isinstance(user, get_user_model()):
        UserDayVisits.objects.get(user=user, day=day).visit_one_more_page()
    else:
        day.anonimous_visits_count += 1
        day.save()
    for day in Day.objects.all():
        visits_count += day.visits_count + day.anonimous_visits_count
    visits_count += 1
    d = dict()
    d['anonimous_visits_today'] = day.anonimous_visits_count
    d['user_visits_today'] = sum(visit.visits_count for visit in UserDayVisits.objects.filter(day=day))
    d['unic_user_visits_today'] = len(UserDayVisits.objects.filter(day=day))
    d['visits_count'] = visits_count
    return HttpResponse(json.dumps(d))
