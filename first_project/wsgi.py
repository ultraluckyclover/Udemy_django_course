"""
WSGI config for first_project project.

# Web Server Gateway Interface - will help us deploy our web app
# to production

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

application = get_wsgi_application()
