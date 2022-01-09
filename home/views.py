from django.shortcuts import render
from django.views import View
from movies.models import Movie
from channels.models import Channel, Schedule
# Create your views here.


class HomePage(View):
    def get(self, request):
        
        
        
        return render(request, 'home/index.html')