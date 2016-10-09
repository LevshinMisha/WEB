from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from task1.settings import AUTH_USER_MODEL


class Day(models.Model):
    date = models.DateField(default=timezone.now, unique=True)
    visits_count = models.IntegerField(default=0)
    visiters = models.ManyToManyField(AUTH_USER_MODEL, through='UserDayVisits')
    anonimous_visits_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.date)


class UserDayVisits(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL)
    day = models.ForeignKey('visits.Day')
    visits_count = models.IntegerField(default=0)

    def visit_one_more_page(self):
        self.user.visits_count += 1
        self.user.save()
        self.day.visits_count += 1
        self.day.save()
        self.visits_count += 1
        self.save()

    def __str__(self):
        return str(self.day) + ' : ' + str(self.user)