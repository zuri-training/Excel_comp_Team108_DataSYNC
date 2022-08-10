"""
WSGI config for authsysproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authsysproject.settings')

django.setup()

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authsysproject.settings')

application = get_wsgi_application()