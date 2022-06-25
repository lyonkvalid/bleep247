from functools import reduce
from operator import or_
from datetime import date
from itertools import chain 

from django.db.models import Q, Count

from rest_framework import viewsets, filters
from rest_framework.response import Response 
from rest_framework.decorators import action 

from django_filters.rest_framework import DjangoFilterBackend

from post.models import Story, Comment
from post.serializers import StorySerializer, CommentSerializer

from account.util import paginate
from account.models import Profile

class StoryViewSet(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    queryset = Story.objects.annotate(clicks_count = Count("clicks__users")).order_by("clicks_count", "date_created")
  
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['topic__topic', 'user__username']

    # returns following authors stories
    @action(["GET"], detail=False)
    def following(self, request, pk=None):
        profile = request.user.profilee
        following_authors_stories = list(chain.from_iterable(list(map(lambda obj: self.queryset.filter(user=obj), profile.following.all()))))
        return paginate(request, self.serializer_class, following_authors_stories)
    
    # return recommended story
    @action(["GET"], detail=False)
    def recommend(self, request, pk=None):
        topics = Topic.objects.filter(following__user=request.user)
        model = None
        if len(topics) == 0:
            model = self.queryset.exclude(user=request.user)
        else:
            query = reduce(or_, [Q(topic__topic=topic.topic, topic__tags__in=topic.tags.all()) for topic in topics])
            model = self.queryset.filter(query).exclude(user=request.user)
        return paginate(request, self.serializer_class, model)
        
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer 
    queryset = Comment.objects.order_by("date_created")