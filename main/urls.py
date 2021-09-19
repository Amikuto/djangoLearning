from django.urls import path, include
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('prices/', views.prices, name="prices"),
    path('about/', views.about, name="about"),
    path('contacts/', views.contacts, name="contacts"),
    path('feedback/', views.feedback, name="feedback"),
]
