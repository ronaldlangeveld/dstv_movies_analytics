from django.contrib import admin
from django.urls import path, include
from . views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home_index'),
]
