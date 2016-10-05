from django.db import models
from django.utils import timezone
from task1.settings import AUTH_USER_MODEL


class Feedback(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(AUTH_USER_MODEL)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def create(self, user):
        self.author = user
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title