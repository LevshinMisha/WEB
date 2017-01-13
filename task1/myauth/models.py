from django.db import models
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from uuid import uuid4


class RegistrationRequestManager(models.Manager):
    def create_registration_request(self, email, username, password):
        rr = self.create(email=email, username=username, password=password, token=uuid4())
        rr.send_email()
        return rr


class RegistrationRequest(models.Model):
    email = models.EmailField()
    username = models.TextField()
    password = models.TextField()
    token = models.TextField()
    objects = RegistrationRequestManager()

    def create_real_user(self):
        return get_user_model().objects.create(username=self.username, password=self.password, email=self.email)

    def send_email(self):
        send_mail('Регистрация на моем сайте', 'Тут такое дело. '
                                               'Кто-то зарегистрировался на моем сайте, указав эту почту. '
                                               'Надеюсь это были вы, потому что я сейчас дам вам ссылку, пройдя по '
                                               'которой вы завершите регистрацию.'
                                               '\nВот же она: {}'.format(self.get_link()),
                  'mishalevshin123@gmail.com',
                  [str(self.email)],
                  fail_silently=False)

    def get_link(self):
        return 'http://levshinmisha.pythonanywhere.com/auth/createUser/{}/{}'.format(self.username, self.token)

    def __str__(self):
        return 'Unregistered User({})'.format(self.username)