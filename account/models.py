from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    uid = models.CharField(max_length=32)
    picture = models.URLField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.uid

"""
    topic following -> if topic in profile.topics following
"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    following = models.ManyToManyField(User, blank=True, symmetrical=False, related_name="following")
    followers = models.ManyToManyField(User, blank=True, symmetrical=False, related_name="followers")
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()