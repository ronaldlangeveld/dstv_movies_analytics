from django.shortcuts import render
from django.views import View
from movies.models import Movie
from channels.models import Channel, Schedule
from django.db.models.functions import TruncMonth, TruncYear, TruncDay
from django.db.models import Count
# Create your views here.


class HomePage(View):
    def get(self, request):
        
        # group movies by the times they are scheduled

        movies = Movie.objects.annotate(num_repeats=Count('movie_schedule')).order_by('-num_repeats')

        
        
        return render(request, 'home/index.html', context={'movies': movies})