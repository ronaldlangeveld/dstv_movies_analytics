from django.contrib import admin
from django.urls import path, include
from . views import MoviesList, MoviesDetail

urlpatterns = [
    path('', MoviesList.as_view(), name='movies_index'),
    path('<pk>', MoviesDetail.as_view(), name='movies_detail'),
]
