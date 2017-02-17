from django.db import models
from django.utils import timezone


class Message(models.Model):
    text = models.CharField(max_length=300)

    @staticmethod
    def delete_old_messages():
        while len(Message.objects.all()) > 10:
            Message.objects.all()[0].delete()

    def __str__(self):
        return str(self.text)