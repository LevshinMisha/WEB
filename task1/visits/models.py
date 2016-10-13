from django.db import models
from django.utils import timezone
from PIL import Image as Img, ImageDraw, ImageFont


class Visit(models.Model):
    ip = models.TextField()
    browser = models.TextField()
    last_hit = models.DateTimeField(default=timezone.now)
    hit_count = models.IntegerField(default=1)

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
        self.img = Img.new("RGBA", (300, 90), (69, 104, 142, 1))
        self.draw = ImageDraw.Draw(self.img)
        self.font = ImageFont.truetype("/usr/share/fonts/opentype/freefont/FreeSansBold.otf", 15)

    def draw_visits(self, today_visits, visits, today_hits, hits):
        self.draw.text((10, 10), "Visits Count: {}\nToday Visits Count: {}".format(visits, today_visits), (255, 255, 255), font=self.font)
        self.draw.text((10, 45), "Hit Count: {}\nToday Hit Count: {}".format(hits, today_hits), (255, 255, 255), font=self.font)
        self.img.save('mysite/static/files/visits.jpg')