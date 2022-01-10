from typing import List
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Movie
from channels.models import Channel, Schedule
from django.db.models.functions import TruncMonth, TruncYear, TruncDay
from django.db.models import Count
from datetime import datetime


# Create your views here.

class MoviesList(ListView):
    model = Movie
    template_name = 'movies/movies_list.html'
    context_object_name = 'movies'
    paginate_by = 100

    def get_queryset(self):
        return Movie.objects.all().order_by('title')


class MoviesDetail(DetailView):
    model = Movie
    template_name = 'movies/movies_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schedule__past'] = Schedule.objects.filter(movie=self.object, show_time__lte=datetime.now()).order_by('-show_time')
        context['schedule__future'] = Schedule.objects.filter(movie=self.object, show_time__gte=datetime.now()).order_by('show_time')
        return context

class RepeatsList(ListView):
    model = Movie
    template_name = 'movies/repeats_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return Movie.objects.annotate(num_repeats=Count('movie_schedule')).order_by('-num_repeats')


class MoviesYearsList(ListView):
    model = Movie
    template_name = 'movies/movies_years_list.html'
    context_object_name = 'movie_years'

    def get_queryset(self):
        years = Movie.objects.all().values('year').annotate(num_movies=Count('year')).order_by('-year')
        return years

class MoviesByYear(ListView):
    model = Movie
    template_name = 'movies/movies_by_year.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return Movie.objects.filter(year=self.kwargs['year']).order_by('title')
    