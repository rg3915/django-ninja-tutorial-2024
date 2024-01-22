from django.conf import settings
from django.contrib import admin
from django.urls import path

from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
]

swagger_urlpatterns = [
    path('api/v1/', api.urls),
]

if settings.SHOW_SWAGGER:
    urlpatterns += swagger_urlpatterns
