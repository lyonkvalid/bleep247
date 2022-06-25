from django.db import models

from taggit.managers import TaggableManager

from account.models import Profile

class Topic(models.Model):
    followers = models.ManyToManyField(Profile, blank=True)
    topic = models.CharField(max_length=16, null=False)
    tags = TaggableManager()
    
    def __str__(self):
        return self.topic

class Image(models.Model):
    alt = models.TextField()
    image = models.ImageField(upload_to="post")
    def __str__(self):
        return self.image.url