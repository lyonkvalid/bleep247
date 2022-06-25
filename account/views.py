import json
from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from django.views.decorators.csrf import csrf_exempt

from .authenticate import firebase_authentication

@api_view(["POST"])
@permission_classes([AllowAny])
def get_token(request):
    data = json.loads(request.body)
    #try:
    user = firebase_authentication(data.get("token"))
    token, created = Token.objects.get_or_create(user=user)
    return Response({
            "token": token.key
    })
    #except Exception as e:
    #return Response({ "error": str(e) }, status=500)