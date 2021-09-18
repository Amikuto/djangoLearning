from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.views.generic.base import RedirectView

from main import views


favicon_view = RedirectView.as_view(url='/static/images/favicon.png', permanent=True)

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('prices/', views.prices, name="prices"),
    path('contacts/', views.contacts, name="contacts"),
    path('feedback/', views.feedback, name="feedback"),
    path('admin/', admin.site.urls),
    re_path(r'^favicon\.ico$', favicon_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
