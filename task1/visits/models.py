from django.db import models
from django.utils import timezone
from PIL import Image as Img, ImageDraw


class Visit(models.Model):
    ip = models.TextField()
    browser = models.TextField()
    last_hit = models.DateTimeField(default=timezone.now)
    hit_count = models.IntegerField(default=1)
    urls = models.TextField(blank=True)

    def add_new_url(self, url):
        if self.urls:
            self.urls += '\n'
        self.urls += url
        self.save()

    def update(self):
        self.last_hit = timezone.now()
        self.hit_count += 1
        self.save()

    def update_only_time(self):
        self.last_hit = timezone.now()
        self.save()

    def __str__(self):
        return str(self.ip) + ', ' + str(self.browser) + ', ' + str(self.last_hit)


class VisitsImage:
    def __init__(self):
        self.img = Img.open('visits.png')
        self.draw = ImageDraw.Draw(self.img)

    def draw_visits(self, today_visits, visits, today_hits, hits):
        self.draw.text((135, 15), "{}".format(visits), (255, 255, 255))
        self.draw.text((135, 45), "{}".format(hits), (255, 255, 255))
        self.draw.text((275, 15), "{}".format(today_visits), (255, 255, 255))
        self.draw.text((275, 45), "{}".format(today_hits), (255, 255, 255))
        return self.img
