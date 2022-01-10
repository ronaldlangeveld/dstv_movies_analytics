from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from movies.models import Movie
from channels.models import Channel, Schedule
from django.db.models.functions import TruncMonth, TruncYear, TruncDay
from django.db.models import Count
from datetime import datetime, date, timedelta
# Create your views here.


class HomeIndex(ListView):
    model = Schedule
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schedule'] = Schedule.objects.filter(show_time__gt=date.today()).order_by('channel', 'show_time').values('channel__name', 'movie__title', 'movie__id', 'show_time', 'end_time')
        context['timestamp'] = datetime.now()
        return context

