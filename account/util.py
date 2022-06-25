import cachecontrol
from google.oauth2.id_token import verify_firebase_token
from google.auth.transport.requests import Request

from rest_framework.pagination import LimitOffsetPagination

def verify_id_token(session, id_token):
    cached_session = cachecontrol.CacheControl(session)
    request = Request(session=cached_session)
    return verify_firebase_token(id_token, request, "bleep247", clock_skew_in_seconds=1000)

def verify_id_token(id_token):
    request = Request()
    return verify_firebase_token(id_token, request, "bleep247")
    
def paginate(request, queryset, serializer_class, many=True):
    paginator = LimitOffsetPagination()
    paginated_queryset = paginator.paginate_queryset(queryset, request)
    serialized_queryset = serializer_class(paginated_queryset, many=True, context={ "request": request })
    return paginator.get_paginated_response(serialized_queryset.data)