from django.shortcuts import render, HttpResponse
import os
from ipware.ip import get_ip
import json
from .models import Visit
from django.utils import timezone
from .models import VisitsImage

TIME_OUT = 30 * 60


def time_to_seconds(time):
    return time.hour * 60 * 60 + time.minute * 60 + time.second


def seconds_to_time(seconds):
    a = timezone.now()
    return a.replace(year=a.year, month=a.month, day=a.day, hour=seconds // (60 * 60), minute=(seconds % (60 * 60)) // 60, second=seconds % 60)


def today_visits():
    return [visit for visit in Visit.objects.all() if visit.last_hit.day == timezone.now().day]


def today_hits():
    return [visit.hit_count for visit in Visit.objects.all() if visit.last_hit.day == timezone.now().day]


def last_visit_was_less_then(ip, browser, time):
    return len(Visit.objects.filter(ip=ip, browser=browser, last_hit__gt=seconds_to_time(time_to_seconds(timezone.now()) - time)))


def visits(request):
    ip = get_ip(request)
    browser = request.META['HTTP_USER_AGENT']
    if last_visit_was_less_then(ip, browser, TIME_OUT):
        visit = Visit.objects.get(ip=ip, browser=browser, last_hit__gt=seconds_to_time(time_to_seconds(timezone.now()) - TIME_OUT))
        if not last_visit_was_less_then(ip, browser, 5):
            visit.update()
        else:
            visit.update_only_time()
    else:
        Visit.objects.create(ip=ip, browser=browser)
    d = dict()
    d['visits_today'] = len(today_visits())
    d['hits_today'] = sum(today_hits())
    d['visits'] = len(Visit.objects.all())
    d['hits'] = sum(visit.hit_count for visit in Visit.objects.all())
    d['time_out'] = TIME_OUT
    return HttpResponse(json.dumps(d))


def visits_img(request):
    a = json.loads(bytes.decode(visits(request).content))
    VisitsImage().draw_visits(a['visits_today'], a['visits'], a['hits_today'], a['hits'])
    return HttpResponse('<img src="/static/files/visits.jpg">')
