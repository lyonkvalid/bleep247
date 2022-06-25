from django.utils import timezone
from django.contrib.auth import get_user_model 

from rest_framework.authentication import BaseAuthentication

from .util import verify_id_token

from .exceptions import NoAuthToken, InvalidAuthToken, FirebaseError

User = get_user_model()

def firebase_authentication(firebase_token):
    decoded_token = None
    assert firebase_token != None, "No authentication token provided"

    try:
        decoded_token = verify_id_token(firebase_token)
    except Exception as e:
        print(e)
        raise InvalidAuthToken("Invalid auth token")

    try:
        uid = decoded_token.get("user_id")
        user, created = User.objects.get_or_create(uid=uid)
        if created:
            user.picture = decoded_token.get("picture")
            user.email = decoded_token.get("email")
            user.email_verified = decoded_token.get("email_verified")
            first_name, last_name = decoded_token.get("name").split(" ")
            user.first_name = first_name
            user.last_name = last_name
            user.username = first_name.lower()
            user.save()
        return user
    except Exception as e:
       print(e)
       raise FirebaseError()