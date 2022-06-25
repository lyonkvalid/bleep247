"""
WSGI config for bleep247 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

import socketio
from sync.views import sio

import eventlet
import eventlet.wsgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bleep247.settings')

application= get_wsgi_application() #StaticFilesHandler(get_wsgi_application())
#application = socketio.Middleware(sio, wsgi_app=application, socketio_path='socket.io')

#eventlet.wsgi.server(eventlet.listen(('', 8000)), application)