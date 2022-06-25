from django.urls import path 

from .views import get_token

urlpatterns = [
    path("token/", get_token)
]