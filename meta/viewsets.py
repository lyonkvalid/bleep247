from itertools import chain 

from django.db.models import Count 

from rest_framework import viewsets
from rest_framework.decorators import action 

from .models import Topic
from .serializers import TopicSerializer
from account.util import paginate

class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.annotate(followers_count=Count("followers")).order_by("followers_count")
    
    def list(self, request, pk=None):
        topics = self.queryset.filter(followers__user=request.user)
        return paginate(request, topics, self.serializer_class)
    
    @action(["GET"], detail=False)
    def recommend(self, request, pk=None):
        profile = request.user.profile
        recommend_following = list(chain.from_iterable(list(map(lambda user: self.queryset.filter(followers__user=user), profile.following.all()))))
        recommend_following.extend(self.queryset)
        return paginate(request, list(set(recommend_following)), self.serializer_class)