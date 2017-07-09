from django.db import models
from django.utils import timezone
from project_root.settings import AUTH_USER_MODEL
import bleach

class Feedback(models.Model):
    text = models.TextField(max_length=500)
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

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        attr = {'a': ['href'], 'img': ['src']}
        self.text = str(bleach.clean(self.text.replace('\n', '<br>'), tags=['img', 'b', 'i', 'a', 'br'], attributes=attr)).replace('\n', ' ')
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.text