from django.contrib import admin
from django.urls import path, include
from . views import MoviesList, MoviesDetail, RepeatsList

urlpatterns = [
    path('', MoviesList.as_view(), name='movies_index'),
    path('repeats', RepeatsList.as_view(), name='movies_repeats'),
    path('<pk>', MoviesDetail.as_view(), name='movies_detail'),
    
]
