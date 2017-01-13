from django import forms
from django.contrib.auth import get_user_model, authenticate
from .models import RegistrationRequest


def user_exists(email):
    return bool(len(get_user_model().objects.filter(email=email)))


def get_username(email):
    try:
        return get_user_model().objects.filter(email=email)[0].username
    except IndexError:
        return None


def get_email(username):
    try:
        return get_user_model().objects.filter(username=username)[0].email
    except IndexError:
        return None


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def is_valid(self):
        return self.check_data() and user_exists(get_email(self.data['username']))

    def authenticate(self):
        return authenticate(email=get_email(self.data['username']), password=self.data['password'])

    def check_data(self):
        for i in ['username', 'password']:
            if i not in self.data:
                return False
        return all(self.data)


class RegistrationForm(forms.Form):
    email = forms.EmailField(max_length=30)
    username = forms.CharField(label='Username', max_length=20)
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput)

    def is_valid(self):
        return self.check_data() and self.data['password1'] == self.data['password2']

    def registrate(self):
        email = self.data['email']
        username = self.data['username']
        password = self.data['password1']
        if len(get_user_model().objects.filter(email=email)) or len(get_user_model().objects.filter(username=username)):
            return 'Пользователь с таким email или username уже существует! Неужто вы спутали кнопку "Войти" с "Регистрация"?'
        if len(RegistrationRequest.objects.filter(email=email)) or len(RegistrationRequest.objects.filter(username=username)):
            return 'Хватит спамить! Если письмо еще не пришло - подождите.'
        RegistrationRequest.objects.create_registration_request(email=email, username=username, password=password)
        return 'На указанную вами почту(надеюсь вы ее не забыли), было выслано письмо. Пройдите по ссылке в письме и регистрация завершится'

    def check_data(self):
        for i in ['email', 'username', 'password1', 'password2']:
            if i not in self.data:
                return False
        return all(self.data)