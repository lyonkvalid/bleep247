from django.contrib.auth import get_user_model 

from rest_framework import serializers 

from account.models import Profile 

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = "__all__"
 
    def get_following(self, obj):
        return obj.following.counts()
    
    def get_followers(self, obj):
        return obj.followers.counts()