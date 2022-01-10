from django.contrib import admin
from django.urls import path, include
from . views import MoviesList, MoviesDetail, RepeatsList, MoviesByYear, MoviesYearsList

urlpatterns = [
    path('', MoviesList.as_view(), name='movies_index'),
    path('repeats', RepeatsList.as_view(), name='movies_repeats'),
    path('years', MoviesYearsList.as_view(), name='movies_years'),
    path('year/<int:year>', MoviesByYear.as_view(), name='movies_by_year'),
    path('<pk>', MoviesDetail.as_view(), name='movies_detail'),
]
