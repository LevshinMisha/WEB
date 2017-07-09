from django.db import models
from project_root.settings import AUTH_USER_MODEL


class Comment(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL)
    text = models.TextField()
    picture = models.TextField()

    def json(self):
        return {'author': str(self.author), 'text': str(self.text)}

    def __str__(self):
        return 'Comment({}, {}, {})'.format(self.author, self.text, self.picture)


class Like(models.Model):
    picture = models.TextField()
    user = models.ForeignKey(AUTH_USER_MODEL)

    def __str__(self):
        return 'Like({}, {})'.format(self.user, self.picture)