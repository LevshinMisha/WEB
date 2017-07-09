import os
from project_settings import project_root, DEBUG, ALLOWED_HOSTS, SECRET_KEY

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WSGI_APPLICATION = project_root + '.wsgi.application'

ROOT_URLCONF = project_root + '.urls'

STATIC_ROOT = os.path.join(BASE_DIR, 'files', 'static')
STATIC_URL = '/static/'