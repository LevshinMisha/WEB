from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Email непременно должен быть указан')

        user = self.model(email=UserManager.normalize_email(email), username=username)

        user.set_password(password)
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class ExtUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Электронная почта', max_length=30, unique=True, db_index=True)
    avatar = models.ImageField('Аватар', blank=True, null=True, upload_to="user/avatar")
    register_date = models.DateField('Дата регистрации', auto_now_add=True)
    is_active = models.BooleanField('Активен', default=True)
    username = models.TextField('Имя Пользователя', unique=True, max_length=20)
    visits_count = models.IntegerField('Кол-во посещений сайта', default=0)

    # Этот метод обязательно должен быть определён
    def get_full_name(self):
        return self.username

    # Требуется для админки
    @property
    def is_staff(self):
        return self.is_superuser

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
