from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path("", views.page, name="login"),
    path("pilihPerbualan", views.pilihPerbualan, name="pilihPerbualan"),
    path("mahuBelajar", views.mahuBelajar, name="mahuBelajar"),
]

# Only in development: serve media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)