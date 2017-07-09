DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_APPS = [
    'mysite',
    'myauth',
    'extuser',
    'feedbacks',
    'visits',
    'gallery',
    'chat'
]

INSTALLED_APPS = MY_APPS + DJANGO_APPS