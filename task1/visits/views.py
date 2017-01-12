from django.shortcuts import HttpResponse
import json
import uuid
from .models import Visit, Visiter, SCREEN_IS_NONE
from django.utils import timezone
import datetime
from .models import VisitsImage

TIME_OUT_FOR_VISIT = 30 * 60
TIME_OUT_FOR_HIT = 5


def get_now():
    return timezone.now()


def time_to_seconds(time):
    return time.hour * 60 * 60 + time.minute * 60 + time.second


def seconds_to_time(seconds):
    date = get_now().date()
    if seconds < 0:
        seconds += 60 * 60 * 24
        date -= datetime.timedelta(days=1)
    return datetime.datetime.combine(date, datetime.time(hour=seconds // (60 * 60), minute=(seconds % (60 * 60)) // 60, second=seconds % 60))


def today_visits():
    return [visit for visit in Visit.objects.all() if visit.last_hit.day == get_now().day]


def today_hits():
    return [visit.hit_count for visit in Visit.objects.all() if visit.last_hit.day == get_now().day]


def last_visit_was_less_then(user_agent, time):
    return len(Visit.objects.filter(user_agent=user_agent, last_hit__gt=seconds_to_time(time_to_seconds(get_now()) - time)))


def visits(request, url):
    def handle_visit(screen, user_agent, visiter):
        if last_visit_was_less_then(user_agent, TIME_OUT_FOR_VISIT):
            visit = Visit.objects.get(user_agent=user_agent, last_hit__gt=seconds_to_time(time_to_seconds(get_now()) - TIME_OUT_FOR_VISIT))
            if not last_visit_was_less_then(user_agent, TIME_OUT_FOR_HIT):
                visit.update()
            else:
                visit.update_only_time()
        else:
            visit = Visit.objects.create(user_agent=user_agent, last_hit=get_now(), visiter=visiter)
        visit.set_screen(screen)

    def handle_visiter(ip, cookie, url):
        if cookie is None:
            cookie = uuid.uuid4()
        if not len(Visiter.objects.filter(ip=ip, cookie=cookie)):
            Visiter.objects.create(ip=ip, cookie=cookie)
        Visiter.objects.get(ip=ip, cookie=cookie).add_new_url(url)
        return HttpResponse(create_visits_info_in_json(cookie)),  Visiter.objects.get(ip=ip, cookie=cookie)

    def create_visits_info_in_json(cookie):
        d = dict()
        d['visits_today'] = len(today_visits())
        d['hits_today'] = sum(today_hits())
        d['visits'] = len(Visit.objects.all())
        d['hits'] = sum(visit.hit_count for visit in Visit.objects.all())
        d['secret_cookie'] = str(cookie)
        return json.dumps(d)

    screen = request.COOKIES.get('screen')
    if screen is None:
        screen = 'JS или куки былы выключены'
    response, visiter = handle_visiter(request.META['REMOTE_ADDR'], request.COOKIES.get('secret'), url)
    handle_visit(screen, request.META['HTTP_USER_AGENT'], visiter)
    return response


def visits_img(request, url):
    if url == '':
        url = '/visits/img/'
    a = json.loads(bytes.decode(visits(request, url).content))
    time = request.COOKIES.get('time')
    if time is None:
        time = 'Никогда'
    response = HttpResponse(content_type="image/png")
    if request.COOKIES.get('secret') is None:
        response.set_cookie('secret', a['secret_cookie'])
    VisitsImage().draw_visits(a['visits_today'], a['visits'], a['hits_today'], a['hits'], time).save(response, "PNG")
    response.set_cookie('time', str(get_now()), path=url[1:])

    return response
