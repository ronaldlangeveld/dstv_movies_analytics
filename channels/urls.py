from django.contrib import admin
from django.urls import path, include
from . views import ChannelList

urlpatterns = [
    path('', ChannelList.as_view(), name='channels_index'),
]
