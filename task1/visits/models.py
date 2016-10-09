from django.db import models
from django.utils import timezone


class Visit(models.Model):
    ip = models.TextField()
    browser = models.TextField()
    last_hit = models.DateTimeField(default=timezone.now)
    hit_count = models.IntegerField(default=1)

    def update(self):
        self.last_hit = timezone.now()
        self.hit_count += 1
        self.save()

    def __str__(self):
        return str(self.ip) + ', ' + str(self.browser) + ', ' + str(self.last_hit)