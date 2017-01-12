from django.shortcuts import HttpResponse
import json
import uuid
from .models import Visit, Visiter
from django.utils import timezone
import datetime
from .models import VisitsImage

TIME_OUT_FOR_VISIT = 30 * 60
TIME_OUT_FOR_HIT = 5


def time_to_seconds(time):
    return time.hour * 60 * 60 + time.minute * 60 + time.second


def seconds_to_time(seconds):
    date = timezone.now().date()
    if seconds < 0:
        seconds += 60 * 60 * 24
        date -= datetime.timedelta(days=1)
    return datetime.datetime.combine(date, datetime.time(hour=seconds // (60 * 60), minute=(seconds % (60 * 60)) // 60, second=seconds % 60))


def today_visits():
    return [visit for visit in Visit.objects.all() if visit.last_hit.day == timezone.now().day]


def today_hits():
    return [visit.hit_count for visit in Visit.objects.all() if visit.last_hit.day == timezone.now().day]


def last_visit_was_less_then(user_agent, time):
    return len(Visit.objects.filter(user_agent=user_agent, last_hit__gt=seconds_to_time(time_to_seconds(timezone.now()) - time)))


def visits(request, url):
    def handle_visit(screen, user_agent, visiter):
        if last_visit_was_less_then(user_agent, TIME_OUT_FOR_VISIT):
            visit = Visit.objects.get(user_agent=user_agent, last_hit__gt=seconds_to_time(time_to_seconds(timezone.now()) - TIME_OUT_FOR_VISIT))
            if not last_visit_was_less_then(user_agent, TIME_OUT_FOR_HIT):
                visit.update()
            else:
                visit.update_only_time()
        else:
            visit = Visit.objects.create(user_agent=user_agent, last_hit=timezone.now(), visiter=visiter)
        visit.set_screen(screen)

    def handle_visiter(ip, cookie, url):
        if cookie is None:
            cookie = uuid.uuid4()
        if not len(Visiter.objects.filter(ip=ip, cookie=cookie)):
            Visiter.objects.create(ip=ip, cookie=cookie)
        Visiter.objects.get(ip=ip, cookie=cookie).add_new_url(url)
        return HttpResponse(create_visits_info_in_json(cookie)),  Visiter.objects.get(ip=ip, cookie=cookie)

    def create_visits_info_in_json(cookie):
        visits_info = {
            'visits': len(Visit.objects.all()), 'visits_today': len(today_visits()),
            'hits': sum(visit.hit_count for visit in Visit.objects.all()), 'hits_today': sum(today_hits()),
            'secret_cookie': str(cookie)}
        return json.dumps(visits_info)

    response, visiter = handle_visiter(request.META['REMOTE_ADDR'], request.COOKIES.get('secret'), url)
    handle_visit(request.COOKIES.get('screen'), request.META['HTTP_USER_AGENT'], visiter)
    return response


def visits_img(request, url):
    if url == '':
        url = '/visits/img/'
    visits_info = json.loads(bytes.decode(visits(request, url).content))
    response = HttpResponse(content_type="image/png")
    VisitsImage().draw_visits(visits_info['visits_today'], visits_info['visits'], visits_info['hits_today'], visits_info['hits'], request.COOKIES.get('time')).save(response, "PNG")
    if request.COOKIES.get('secret') is None:
        response.set_cookie('secret', visits_info['secret_cookie'])
    response.set_cookie('time', str(timezone.now()), path=url[1:])
    return response
