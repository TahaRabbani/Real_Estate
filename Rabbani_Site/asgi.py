"""
ASGI config for Rabbani_Site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

# Importing the 'os' module to interact with the operating system
import os
# Importing the ASGI application handler from Django
# This is used for handling asynchronous server communications
from django.core.asgi import get_asgi_application
# Importing the ASGI application handler from Django
# This is used for handling asynchronous server communications
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rabbani_Site.settings')
# Getting the ASGI application callable
# This is the entry point for ASGI-compatible web servers (e.g., Daphne, Uvicorn) 
# to serve your Django application
application = get_asgi_application()
