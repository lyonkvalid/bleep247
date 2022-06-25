from rest_framework import viewsets
from rest_framework.response import Response

from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Profile.objects.all()

    def list(self, request, pk=None):
        return Response(self.serializer_class(request.user).data)

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def list(self, request, pk=None):
        return Response(self.serializer_class(request.user.profile).data)