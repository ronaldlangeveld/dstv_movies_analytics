from django.contrib import admin
from django.urls import path, include
from . views import HomeIndex

urlpatterns = [
    path('', HomeIndex.as_view(), name='home_index'),
]
