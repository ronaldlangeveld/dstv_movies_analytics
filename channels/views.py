from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Movie, Channel, Schedule
from django.db.models.functions import TruncMonth, TruncYear, TruncDay
from django.db.models import Count
# Create your views here.

class ChannelList(ListView):
    model = Channel
    template_name = 'channels/channels_list.html'
    context_object_name = 'channels'

    def get_queryset(self):
        return Channel.objects.all().order_by('id')



# Show Schedule for Channel grouped by month\day

class ChannelDetail(DetailView):
    model = Channel
    template_name = 'channels/channel_detail.html'
    context_object_name = 'channel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schedules'] = Schedule.objects.filter(channel=self.object).order_by('show_time').annotate(month=TruncMonth('show_time'), day=TruncDay('show_time'), year=TruncYear('show_time'))
        print(context['schedules'])
        return context
    
