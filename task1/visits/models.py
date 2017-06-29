from django.db import models
from django.utils import timezone
from PIL import Image, ImageDraw, ImageFont

SCREEN_IS_NONE = 'JS или куки былы выключены'


class Visit(models.Model):
    user_agent = models.TextField()
    screen = models.TextField(default=SCREEN_IS_NONE)
    last_hit = models.DateTimeField(default=timezone.now)
    hit_count = models.IntegerField(default=1)
    visiter = models.ForeignKey('Visiter')

    def update(self):
        self.last_hit = timezone.now()
        self.hit_count += 1
        self.save()

    def update_only_time(self):
        self.last_hit = timezone.now()
        self.save()

    def set_screen(self, screen):
        if screen != SCREEN_IS_NONE and screen is not None:
            self.screen = screen
            self.save()

    def __str__(self):
        return 'Visit(screen={}, user_agent={}, last_hit={}, visiter={})'.format(self.screen, self.user_agent, self.last_hit, self.visiter)


class Visiter(models.Model):
    cookie = models.TextField()
    ip = models.TextField()
    urls = models.TextField(blank=True)

    def add_new_url(self, url):
        self.urls += url + '\n'
        self.save()

    def __str__(self):
        return 'Visiter(ip={}, cookie={})'.format(self.ip, self.cookie)


class VisitsImage:
    def __init__(self):
        self.img = Image.new('RGB', (300, 100), (69, 104, 142))
        self.draw = ImageDraw.Draw(self.img)
        self.draw.font = ImageFont.truetype('Pillow/Tests/fonts/DejaVuSans.ttf', 15)

    def draw_visits(self, today_visits, visits, today_hits, hits, time):
        if time is None:
            time = 'Никогда'
        self.draw.text((5, 5), 'Визитов:')
        self.draw.text((5, 30), 'Посещений:')
        self.draw.text((150, 5), 'Сегодня:')
        self.draw.text((150, 30), 'Сегодня:')
        self.draw.text((5, 55), 'Эта страница была посещена:')
        self.draw.text((100, 5), str(visits))
        self.draw.text((100, 30), str(hits))
        self.draw.text((230, 5), str(today_visits))
        self.draw.text((230, 30), str(today_hits))
        self.draw.text((5, 80), str(time))
        return self.img