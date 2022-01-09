from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Movie
from channels.models import Channel, Schedule



# Create your views here.

class MoviesList(ListView):
    model = Movie
    template_name = 'movies/movies_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return Movie.objects.all().order_by('title')


class MoviesDetail(DetailView):
    model = Movie
    template_name = 'movies/movies_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schedule'] = Schedule.objects.filter(movie=self.object)
        return context
