from django.shortcuts import HttpResponse
from ipware.ip import get_ip
import json
from .models import Visit
from django.utils import timezone
from .models import VisitsImage

TIME_OUT_FOR_VISIT = 30 * 60
TIME_OUT_FOR_HIT = 5


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


def visits(request, url):
    def handle_visit(ip, browser):
        if last_visit_was_less_then(ip, browser, TIME_OUT_FOR_VISIT):
            visit = Visit.objects.get(ip=ip, browser=browser, last_hit__gt=seconds_to_time(
                time_to_seconds(timezone.now()) - TIME_OUT_FOR_VISIT))
            if not last_visit_was_less_then(ip, browser, TIME_OUT_FOR_HIT):
                visit.update()
            else:
                visit.update_only_time()
        else:
            visit = Visit.objects.create(ip=ip, browser=browser)
        return visit
    
    def create_visits_info_in_json():
        d = dict()
        d['visits_today'] = len(today_visits())
        d['hits_today'] = sum(today_hits())
        d['visits'] = len(Visit.objects.all())
        d['hits'] = sum(visit.hit_count for visit in Visit.objects.all())
        return json.dumps(d)
    
    handle_visit(get_ip(request), request.META['HTTP_USER_AGENT']).add_new_url(url)
    return HttpResponse(create_visits_info_in_json())


def visits_img(request, url):
    a = json.loads(bytes.decode(visits(request, url).content))
    time = request.COOKIES.get('time')
    if time is None:
        time = 'Никогда'
    img = VisitsImage().draw_visits(a['visits_today'], a['visits'], a['hits_today'], a['hits'], time)
    response = HttpResponse(content_type="image/png")
    response.set_cookie('time', str(timezone.now()))
    img.save(response, "PNG")
    return response
