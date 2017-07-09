"""
WSGI config for task1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from .settings import project_root

os.environ.setdefault("DJANGO_SETTINGS_MODULE", project_root + ".settings")

application = get_wsgi_application()
