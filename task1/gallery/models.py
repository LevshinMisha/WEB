from django.db import models
from task1.settings import AUTH_USER_MODEL


class Comment(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL)
    text = models.TextField()
    picture = models.TextField()

    def to_json(self):
        return {'author': str(self.author), 'text': self.text}

    def __str__(self):
        return 'Comment({}, {}, {})'.format(self.author, self.text, self.picture)