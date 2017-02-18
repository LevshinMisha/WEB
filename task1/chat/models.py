from django.db import models
import bleach


class Qwe:
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        attr = {'a': ['href'], 'img': ['src']}
        self.text = str(
            bleach.clean(self.text.replace('\n', '<br>'), tags=['img', 'b', 'i', 'a', 'br'], attributes=attr)).replace(
            '\n', ' ')
        return super().save(force_insert, force_update, using, update_fields)


class Message(models.Model):
    text = models.CharField(max_length=300)

    @staticmethod
    def delete_old_messages():
        while len(Message.objects.all()) > 10:
            Message.objects.all()[0].delete()

    def json(self):
        return {
            'text': str(self),
            'id': self.id,
        }

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.text = str(bleach.clean(self.text, tags=[], attributes={}))
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return str(self.text)