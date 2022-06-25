from rest_framework import serializers

from .models import Topic 
from post.models import Story 
from account.serializers import UserSerializer 

class TopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        exclude = ("followers", )