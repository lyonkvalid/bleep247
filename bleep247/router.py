from rest_framework import routers

from meta.viewsets import TopicViewSet
from post.viewsets import StoryViewSet, CommentViewSet
from account.viewsets import UserViewSet, ProfileViewSet

router = routers.SimpleRouter()

router.register(r"story", StoryViewSet)
router.register(r"comment", CommentViewSet)


router.register(r"user", UserViewSet)
router.register(r"profile", ProfileViewSet)

router.register(r"topic", TopicViewSet)