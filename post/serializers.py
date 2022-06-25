from datetime import datetime
from django.contrib.humanize.templatetags.humanize import naturaltime, naturalday

from rest_framework import serializers 

from post.models import Story, Comment

class StorySerializer(serializers.ModelSerializer):
    preview_image = serializers.SerializerMethodField('get_preview_image')
    class Meta:
        model = Story
        exclude = ("text",)

    def get_preview_image(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.preview_image.image.url)
    
    def get_created_date(self, obj):
        return naturalday(obj.created_date) if (datatime.now() - obj.created_date) > 1000 * 60 * 24 else naturaltime(obj.created_date)
    
    def get_likes(self, obj):
        return obj.likes.counts()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ("story", "comment" )
    
    def get_likes(self, obj):
        return obj.likes.counts()