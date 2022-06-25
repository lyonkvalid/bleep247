from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

from taggit.managers import TaggableManager

from meta.models import Topic, Image

User = get_user_model()

MODEL_NAMES = (
    ("STORY", "STORY"),
)

# model use for analytic and recommendation purpose
class Click(models.Model):
    users = models.ManyToManyField(User, blank=True)
    index_name = models.CharField(choices=MODEL_NAMES, max_length=16)
    
    def __str__(self):
        return self.index_name

class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=101)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=101)
    preview_image = models.ForeignKey(Image, on_delete=models.CASCADE)
    text = MarkdownField(rendered_field='text_rendered', validator=VALIDATOR_STANDARD)
    text_rendered = RenderedMarkdownField()
    clicks = models.ForeignKey(Click, on_delete=models.CASCADE, blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="story_likes", blank=True)
    keywords = TaggableManager()
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=101)
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)
    comment = models.ForeignKey("self", on_delete=models.CASCADE, related_name="child_comment")
    def __str__(self):
        return self.story.title