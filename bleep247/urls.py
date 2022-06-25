from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("auth/", include("account.urls"))
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)