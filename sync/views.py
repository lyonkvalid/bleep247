import os

from django.http import HttpResponse

import socketio

async_mode = None

sio = socketio.Server(async_mode=async_mode)
thread = None

@sio.event
def connect(sid, environ, auth):
    print(f"connectted .... socket {sid}")