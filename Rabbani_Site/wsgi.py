"""
WSGI config for Rabbani_Site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
# Importing the 'os' module to interact with the operating system
import os
# Importing the WSGI application handler from Django
from django.core.wsgi import get_wsgi_application
# Setting the default settings module for the Django project
# 'Rabbani_Site.settings' is the Python path to your project's settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rabbani_Site.settings')
# Getting the WSGI application callable for serving the Django project
# This is the entry point for WSGI-compatible web servers to serve your application
application = get_wsgi_application()
