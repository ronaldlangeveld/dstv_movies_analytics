from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Movie, Channel, Schedule
# Create your views here.

class ChannelList(ListView):
    model = Channel
    template_name = 'channels/channels_list.html'
    context_object_name = 'channels'

    def get_queryset(self):
        return Channel.objects.all().order_by('id')