from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.views.generic.base import RedirectView

from main import views


favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('admin/', admin.site.urls),
    re_path(r'^favicon\.ico$', favicon_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
