from django.contrib import admin
from django.urls import path, include
from . views import ChannelList, ChannelDetail

urlpatterns = [
    path('', ChannelList.as_view(), name='channels_index'),
    path('<pk>', ChannelDetail.as_view(), name='channel_detail'),
]
