"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application
from configurations import importer
import configurations
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      config('DJANGO_SETTINGS_MODULE', cast=str))
os.environ.setdefault('DJANGO_CONFIGURATION',
                      config('DJANGO_CONFIGURATION', cast=str))
configurations.setup()


application = get_wsgi_application()

